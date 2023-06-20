--- 
title: 'Applying large language models for specialized tasks: Can AI suggest you a course?'
author: Donatas Vaiciukevičius
project_authors: Donatas Vaiciukevičius, Anton Zaliznyi, Dzvenymyra-Marta Yarish
editors: GPT-3.5, Github Copilot
---

# {% $markdoc.frontmatter.title %}

Author: {% $markdoc.frontmatter.author %}
Project authors: {% $markdoc.frontmatter.project_authors %}
Editors: {% $markdoc.frontmatter.editors %}

## Introduction

The release of OpenAI's ChatGPT has shaken up the ML community (and to a lesser degree, the entire humankind). It's ability to appear intelligent by replying to given prompts, understanding context between message chains and ability to produce truthful-looking text was mind-boggling. Although the hype has somewhat died off for now in the general public, ML researchers are actively exploring ways to create, optimize and use similar language models.

Inspired by this, we wanted to see how the technology could be used in more specified tasks. We decided to try and create a language model based assistant, who would be able to answer questions about the courses in the University of Tartu. We believed it would be a great way to test the limits of the technology.

## Why does it matter?

Selecting courses for the next semester is a daunting task for every student. You have to consider the topics, workload, schedules and a lot of other factors - it's easy to get lost in the sea of information. You need to hurry as well, as the available places are usually limited. The decision is important, you will be committing a lot of time and effort towards the courses you choose. There's always opportunity cost to consider as well, so all in all it's a very important decision. This means that any help with the decision making is very welcome.

However, universities are not always the best at providing this help. The information is usually scattered across multiple websites, there is a lot of it, and it can be difficult to answer a particular question. In theory, this where an AI assistant could come in handy. It could answer questions about the courses, help you find the information you need and even suggest courses based on your preferences. Nobody would really get hurt - the students would get better guidance while there's no real downside for the university. It's not like someone is hired particularly to answer these questions anyway.

## Where do we start?

It's one thing to play around with models like ChatGPT, but creating a specialised one is an entirely different beast. It is nice that we have the entire natural language processing academic community to take examples from. One of the models that has gotten a lot of attention last couple of months is LLaMA from Meta. Initially, the model weights have been released to academic institutions only, but it only took two weeks for someone to create a torrent and share it on 4chan. At the moment there are tens if not hundreds of variations of the initial models fine-tuned on different datasets, floating around the internet. We decided to do the same and fine-tune the model on the course descriptions from the University of Tartu. What is fine-tuning you may ask - it's a process of taking a model that was already trained and is capable of performing some task, but then training it further to perform something better or different. 

## How do we get this data?

As students of the University of Tartu, we were able to access the LLaMA model weights. However, we still needed the data to fine-tune it on. We tried consulting ChatGPT about how to proceed, and it suggested web scraping the university website. It's a decent guess, but the approach involves a lot of data cleaning and luckily it turned out that the major source for information about the courses in UT [ÕIS](https://ois2.ut.ee), has an API. After a little bit of stumbling around the endpoints available, we were able to find the one we needed. We wrote a script to find all the courses with information available in the system, and then query information about each specific course.

```python
def get_all_courses():
    courses = []
    parameters = {
        'start': 1,
        'take': 300,
        }
    received = 300
    while parameters['take'] == received:
        response = requests.get(f'{base_address}/courses', parameters)
        received = len(response.json())
        courses += response.json()
        parameters['start'] += parameters['take']
        print(f'Collected {len(courses)} courses')
    
    return courses

def get_course_latest_details(course):
    return requests.post(f'{base_address}/courses/course-version/{course["latest_version_uuid"]}').json()
```

*Getting course data from ÕIS API*

However, it turned out that this was the easy part. The data was very messy - each course is represented by a JSON file with tens of fields that contain a lot more nested objects. We wrote a lot of code to extract the data we deemed useful, however it seemed the deeper you went, the more inconsistencies you found. 

For example, a lot of objects with textual information had two nested fields - one for Estonian `et` and one for English `en`. Cool, right? Well in reality sometimes only one of the fields were present, sometimes it was both and sometimes - neither. And that would be fine, but sometimes the `en` field would actually contain Estonian text and vice versa!

We did our best to handle these edge cases and in the end we ended up with a (relatively) clean dataset of 2969 courses. There was the last hurdle before fine-tuning though - the model should be trained on chat-like examples - essentially question-answer pairs in our case. But all we had was JSON files with fields like `course_language`, `lecturers`, `credit_amount` and so on.  First idea was to use ChatGPT for this - we fed it the JSON file and it generated a lot of questions and answers. However, we noticed that they didn't match the given JSON every time, it seemed that the GPT model was more interested in generating text that sounded good, rather than being factually correct. For example, sometimes even though the JSON file said that the course taught in Estonian, the model would generate an answer that "The course is in English". Getting the questions to our local machine would also be a problem - OpenAI's API is quite pricey for our student budget, and web scraping would add a lot of work (and would likely break some terms of service).

In the end, we realised we'd have to generate the questions by ourselves. For that, we ended up using some predefined question-answer patterns and filling them with the data from the JSON file. For example, a template could be `"What faculty is the course {course_name} taught at? The course is taught at the {faculty_name}"`. This way we generated more than 151k question-answer pairs.

## Fine-tuning

Now that we had the data, we could finally fine-tune the model. Or could we? There was a different problem. The model, as the name suggests, was huge, the smallest one containing around 7 billion parameters (almost a parameter per person currently alive). More so, this model was initially trained for 82 432 GPU-hours, just to give you a point of reference that's more than 9 years on a single GPU. We didn't have the luxury of such resources. Luckily, there was a way.

We stumbled upon adapters - a way to train a model on a new task without changing the original weights. The way it works is that you take a pre-trained model, freeze its weights and then add some small trainable layers in-between the original ones. This way you only train these new layers, which essentially take up the task of transforming the outputs of the original model so that they fit the new task. After this new discovery, fine-tuning went swimmingly and only took around 10 hours on a single GPU in the university's HPC cluster.

## Success?

After fine-tuning, we could finally test the idea and see if our effort was worth it. Spoiler alert - we were about to be disappointed.

At first, the results seemed promising. The model has learned the questions and the answers and was ready to respond with an answer that looked convincing enough. For example:

```
Q: How many credits can I get for the course "Design and analysis of algorithms" ?
A: For the course Design and analysis of algorithms you can get 3 credits.
```

The problem was the course was actually worth 6 credits... The model has learned the general answer structure, but being truthful and precise was still an issue. Let's think a bit why that is.

As you probably already now, under the hood the model is just a lot of numbers, connected with one another by mathematical operations. The model is trained to adjust these numbers so that the output of the model is as close to the desired output as possible. In our case, the desired output is the answer to the question (a numerical representation of the words of that answer, to be precise). The way a transformer model works is that it predicts the next word in the answer based on the question (query) as well as the so far generated words (output). That is done iteratively, therefore the generated answer goes:

```
Q: 'How many credits can I get for the course "Design and analysis of algorithms" ?'

A: 'For' -> 'For the' -> 'For the course' -> 'For the course Design' -> ....
```

The problem is, the model doesn't know what the answer should be, it just knows that it should be as close to the desired answer as possible. Therefore, it can't really know if the answer is correct or not. During training, the most common amounts of credits were either 3 or 6, therefore the model learned to generate these numbers. However, it didn't learn that the course "Design and analysis of algorithms" is worth 6 credits, it just learned that the most common answer for a similar question is 3 or 6.

The model was also very keen to hallucinate when the question was something it hadn't seen during training - for example:

```
Q: What is the purpose of taking care of llamas course?
A: The purpose of the course Llamas as Pets is to provide the students with practical knowledge and skills in the field of veterinary medicine.
```

Even though the course doesn't exist...

## So, what now?

It was obvious that the approach didn't work - LLaMA model was shown to perform well in numerous fine-tuning scenarios, but in order to have a useful assistant we needed truthfulness and precision. We had to go back to the drawing board. And technique we discovered was a lot more promising.

The new approach still involved a large language model - this time Vicuna, a variation of LLaMA fine-tuned on user's conversations with ChatGPT, of all things. However, this time we didn't fine-tune the model, we used it as-is. The idea was to give the model some context about the course and then ask it to generate a question about it. In this situation the task would be to just to extract the answer from the given context, which is a lot easier and more precise than trying to predict it out of thin air.

The problem is the context size of the model (the number of word tokens you can feed it as an input) is limited - 5120 tokens for the Vicuna-13B model we used. This means that we cannot possibly feed it the whole JSON of a single course, let alone the entire dataset. Therefore, we had to come up with a way to represent the course in a way that is both concise and informative. We ended up with a simple solution - we took the same approach of creating patterns for each field, however this time it was to construct a document about the course instead of a question and answer. For example, the pattern for the course name could be `"The course {course_name} is taught at the {faculty_name} faculty and is worth {credit_amount} credits."`. This way we could represent the course in a way that is both informative and concise. It was also a way to transform the data into a more human-like format, which is more similar to what the model was trained on in the first place.

What we also decided to do was add some documents about the lecturers of the university. It was a simple pattern - `Lecturer {lecturer_name} teaches the courses {courses}`. In theory this should help the end user if, for example, they took a course from some lecturer and would (or wouldn't) like to take other courses from them. A small side effect of this was that there are a lot of lecturers, sometimes multiple per course, and these documents skewed the overall document size distribution. It could become a problem at some point, but it seemed fine at the time.

![Document size distribution](images/using_big_language_models_course_choice/document_sizes.svg)

*Document size distribution histogram shows how adding the lecturer makes the distribution imbalanced*

However, all of these documents still would not fit into the context of the model, we needed a way to pick the most important ones, based on the given question. We opted to use cosine similarity for this search. What's cosine similarity you might ask. The metric is used to compare how aligned two multidimensional vectors are. If we have vectors $a$ and $b$, the cosine similarity is defined as:

$$similarity = ∑(a_i * b_i) / (√(∑(a_i^2)) * √(∑(b_i^2)))$$

*Computing cosine similarity*

Here the resulting value is 1 when the vectors are identical and -1 when they are completely opposite. The hope is that the vector representing the question would be most similar to the vector representing the document that contains the answer. Unfortunately, that's not always the case - models used for embedding generation usually have a bias towards certain features of the text that is being encoded. In our case, the issue came with the models being biased towards the length of the text, and the embeddings for the question would be most similar with the ones for the shortest known document. Fortunately, we found an embeddings model which was length-agnostic - [`INSTRUCTOR Transformer`](https://arxiv.org/pdf/2212.09741.pdf). 

## The data journey

Before we proceed, let's take a little bit of time to think about what we achieved here. We started with (relatively) dirty data coming in from the ÕIS API, cleaned it up to get rid of all the meaningless, indistinguishable or duplicate data. Afterwards, we took this data and transformed it into two different formats - questions and documents. 

![Data flow schema](images/using_big_language_models_course_choice/data_flow.svg)

*Flow of the data throughout the process*

The two different modalities show two different approaches of working with this data - the question-based approach attempts to encode the information in the model itself, meaning it's operation would be quicker and relatively straightforward. However, as we have seen before, we lose precision this way.

The document-based approach ideally keeps all the information we want, and in theory can be as precise as the documents themselves. It also allows to update the data inexpensively as the model is not changed, only the documents are. However, it is a lot slower and more expensive to operate, as we need to do perform document search first.

## There are some trade-offs

So, the issue with embeddings was solved - the question about the course $x$ would be the most similar to the document about the course $x$. At least most of the time. Sometimes it would be 2nd or third most similar. So we opted to take the top 3 most similar documents. Why 3 exactly? Well, we still had the limit of the context size, and we had to fit the question in it as well. This raised a question - how big can we make the documents? 

It turned out to be a more difficult question than expected - the documents varied in size a lot depending on how big the descriptions were, how many fields were filled-in, etc. The problem occurred when a couple of big documents would get selected as the most similar ones. In some cases, they would not fit into the context properly, not all the information was there and the model would get confused. In the end, we decided to simply limit the number of fetched documents to 3 and hope for the best. I'd prefer to have a more elegant solution, but it was the best we could do in the time we had.

## Conditioning

There was one last thing. We had to condition the model to do exactly what we wanted it to do - answer the question based on the given documents. Essentially that meant we had to come up with a prompt that would make sure the model answers the question while hopefully also making sure it doesn't generate anything unrelated to the University of Tartu. We ended up with the following prompt:

```
Your job is to answer student questions about the University of Tartu. You have to answer based on some information given below. If there is no relevant information, you should tell the student that you do not know the answer. Do not reveal any details of how question answering process works. Do not mention the information given to you. When possible, rephrase the answer so it follows the grammar rules well, flows naturally and is easy to understand. Only use the context from the paragraph that is relevant to the question the most. Only answer the question that is asked. Do not add any additional information.
```

Following the rules in the prompt turned out to be a more difficult task for the model than initially expected. At first, we were using the 7 billion parameter Vicuna counterpart, however it was highly sensitive to the slightest changes in the prompt and extremely unreliable. For example, switching from `Do not answer unrelated questions` to `Don't answer unrelated questions` would cause the model to completely disregard these instructions. The 13 billion parameter model was a lot more robust in our testing, so we settled on that.

## The question answering pipeline

With this approach, there was a lot of moving parts - creating the embeddings database, generating embeddings for the given question, picking documents based on similarity, constructing the full prompt, generating the answer and finally post-processing it back to readable text. We had to make sure that all of these parts work together seamlessly. Luckily, we came across a great framework called [LangChain](https://python.langchain.com/en/latest/index.html).

LangChain is a framework for building applications powered by language models. It has a lot of built in functionality and I don't believe we explored even 10% of it. Still, it was a great tool. Essentially what we had to do was:
* Define classes with our own custom logic for the embeddings model and the question answering model.
* Create a database for the embeddings model. LangChain has great compatibility with ChromaDB - a database that is free, open-source and built specifically for storing embeddings.
* Plug-in the conditioning prompt template for the QA model. Apart from the conditioning prompt it included some placeholders such as `<context>` and `<question>` which would be replaced with the actual context and question during runtime.

```python
document_df = pd.read_csv(f'{shared_dir}/data/documents.csv')
loader = DataFrameLoader(document_df, ["text"])
text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=0)
embeddings_model = InstructorEmbeddingsWrapper()
documents = loader.load()
texts = text_splitter.split_documents(documents)

db = Chroma.from_documents(texts, embeddings_model)

llm = VicunaModelWrapper()

llm_prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

retriever = db.as_retriever(search_kwargs={"k": 3})
chain_type_kwargs = {"prompt": llm_prompt}

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff" \
    , retriever=retriever, chain_type_kwargs=chain_type_kwargs)
qa.combine_documents_chain.document_prompt = conditoning_prompt

query = "What courses should I take to learn python?"
response = qa(query)
```

*Essential parts of the pipeline (with some variable initialization skipped for clarity)*

And that's about it. In the end the couple lines of code for the pipeline didn't look like much, but it took a lot of time and effort to get there. But does it work?  

## Results! 

Finally, we got to the point where all the cogs were in place and we could start testing. And it was great! The pipeline could generalize to questions well, it was able to answer questions about specific courses and even lecturers.

```
Q: What courses can I take if I want to learn natural language processing?
A: You can take the course Natural Language Processing offered by the Chair of Natural language Processing at the University of Tartu. This course covers contemporary natural language processing tasks and methods, including language modelling, text classification, and sequence models, and is taught using deep-learning techniques with recurrent and attention-based neural networks. The course is offered in the 2023/2024 academic year and is open to master and doctoral level students. Alternatively, you can take the course Language Technology offered by the Chair of Natural Language Processing at the University of Tartu.
```

It was really impressive, and the conditioning prompt worked well most of the time as well. However, there were still some issues upon closer inspection. Despite the conditioning, some topics in the responses would sometimes go outside the bounds of University of Tartu. It would also sometimes reply to questions that were off topic. The responses were quite nice in general, but if you plan to deploy the model on the university website, you probably wouldn't want it to discuss politics or religion.

The worst, however, were the cases were the answer would still be unreliable. For example, in some cases it would get confused and make up a course based on documents related to two different courses. Investigation later has shown that it would be the case when the documents were so large, that the conditioning prompt would get cut off. So, there's definitely room for improvement. 

```
Q: How many credits will I get from Introduction to Healthy Eating course?
A: The course named 'Nutraceuticals, Home Artificial Nutrition and Financial Aspects' has 6 credits.
```

## How to evaluate it though?

The question answering pipeline looked reliable most of the time. That's the problem - **most**. There were so many different questions possible that it was impossible to be sure. We started to wonder if there's a way to evaluate the accuracy of the model automatically. The general metrics we used before were no good for this task. For example, F1 score is usually very good for evaluation of classification problems - it calculates a harmonic mean of precision and recall ([Google developers](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) website has a great reminder about them). However, if we used it here, it would mean that the generated answer would have to match the real one word to word, so for example answers `Course is worth 6 ECTS` and `You can earn six credits for the effort` would be considered completely different, which is not what we want.

$$F1=2{\frac {\mathrm {precision} \cdot \mathrm {recall} }{\mathrm {precision} +\mathrm {recall} }}={\frac {2\mathrm {tp} }{2\mathrm {tp} +\mathrm {fp} +\mathrm {fn} }}$$

*Computing the F1 score(Here tp = true positives, fp = false positives and fn = false negatives)*


And here what helped us was actually another language model! At some point we got a bit hopeless while trying to find the solution for evaluation, so we tried asking ChatGPT. We gave it a description of our pipeline, and gave an idea very quickly - using cosine similarity - the same approach we used for picking the documents. In this case, we would compare the generated answer with the real answer and see how similar they are. And we even had questions generated already for the first fine-tuning attempt! Great, right?

Well, turns out it's not that simple. Cosine similarity was great while picking the documents, but it didn't work that well for the answers. Even if the answer was not correct, it was still relatively similar to the real answer with its semantic meaning - sentences `The course is offered for the Master's level students.` and `The course is offered for the Bachelor's or Masters' level students` would be considered very similar. We are still talking about the same domain - academics, and while the answer is not correct, it is very close. It meant that even after trying out a lot of different embedding models, we couldn't get a reliable evaluation metric. The Bi-encoder model had the most distinct difference between the results of the fine-tuning and retrieval augmentation, so we chose that as the cosine-similarity baseline. However, what it showed was that the fine-tuning approach was better! It was surprising at first, but it made sense upon further investigation. If you remember the fine-tuning results, our model learned the patterns of the answers, but not the information behind them. Well, these patterns were what also tricked the cosine similarity metric - the answers were similar enough to be considered good, while not being correct. It's the opposite of the F1 score issue - now the answers were too similar.

We can visualise this problem using principal component analysis. It's a technique that is used to reduce the dimensionality of the embedding vectors, while still keeping the most important information. We can reduce the vectors even to two dimensions, which allows us to plot them on a graph as points. As you can see below, there's a lot of overlap between the embedding vectors of the real answers, and ones generated by our fine-tuned model. There are no clear clusters, meaning that all the answers are really similar. We know that there are wrong answers in there, as we have tried out the model by ourselves, but the cosine similarity metric can't tell a huge difference between them.

![Answer embeddings PCA](images/using_big_language_models_course_choice/answer_pca.svg)

*Answer distribution visualised in 2D space using PCA*

It turns out we are not the only ones dealing with such issues and evaluating text generation models is still an open problem in the field. However, one of the most popular approaches is using [BERTScore](https://arxiv.org/pdf/1904.09675.pdf). It's a combination of the previously mentioned approaches - cosine similarity and F1 score - however here the idea is to compare the matches not of the generated sentence structure, but of the vectors representing the word meaning instead. Each word vector from the prediction gets compared with a vector from the ground truth, and afterwards pairs are created based on the highest cosine similarity match. afterwards, the F1 score is calculated based on these pairs.

It's a great approach, at least on paper. In reality, however, it wasn't much better at evaluating our work - the scores, as you can see below, told the same story.

|          |  Bi-Encoder cosine similarity   |  BERTScore  |
|:-----------:|:-------------:|:-----------:|
| Fine-tuning |  0.978 | 0.977      |
| Retrieval augmentation |    0.94   |   0.921       |

*Quantitative evaluation of the fine-tuning and retrieval augmentation approaches*

At this point we started giving up on automated evaluation. We ran out of ideas, and consulting online sources or language models essentially had us running in circles - the approaches we found or were suggested relied on the same underlying principles and therefore would suffer from the same problems as well.

## Conclusion

It was a bit disappointing to say the leas - we had no quantitative proof that our pipeline is a better approach (or works well in general). However, we still had the qualitative results we got by just interacting with the pipeline ourselves. And, despite the hallucinations every once in a while, they were still pretty impressive. More importantly, they showed that the idea of using a language model for course selection guidance is a feasible idea. It's not perfect and it's definitely not ready to be deployed on the university website, but it's a great start. Given some more time and resources, it looks like it could be improved to the point where it could be used in production.

Furthermore, what the project has shown us is the power of the academic and open-source communities. A lot of the ideas we used, starting from the model itself coming from Meta's researchers, ending with LangChain, a framework started by a single developer as a personal open project. We also couldn't have done it without all the information available in the public research papers and blogs. It's a great reminder that the best way to learn is to learn not only from yourself, but from others as well, and, more importantly, not to reinvent the wheel.

### *Epilogue*

Although this project initially started as a part of relatively unrelated course, it thought me a lot about the data thinking journey. I believe parts of it was already there, formed through the years of previous academic and work experience. However, the data thinking course made me realise that a lot of the barriers we put on ourselves while working on one or another research problem are artificial. It's not that we actually have all the knowledge and skills to achieve results in any topic, no. Very often though, all that is available, we just need to get in a mindset where we don't stop asking questions, cutting up big questions into small chunks and working on them one by one. Especially these days when we can get a lot of help from the newest large language models. It's not perfect by any means, but they can be a good tool for generating ideas or getting a better understanding of the problem. We got stuck again and again and again working on this project. It's discouraging, especially when you think that you did everything you could, you took the same steps someone else did, and you should be getting results at this point. Unfortunately, that's not how it goes most of the time. You have to put your head down, clear your mind ant try again. And that's what data thinking is about - asking questions, thinking about the information available, iteratively making the best decision we see fit and not giving up. And that's what I'm going to take with me from this course.

### P.S.

If you want to explore the code written for data extraction, fine-tuning, question answering pipeline, evaluation and visualisations, you can find it in the [GitHub repository](https://github.com/DzvinkaYarish/tartu-nlp-courses-qa).
