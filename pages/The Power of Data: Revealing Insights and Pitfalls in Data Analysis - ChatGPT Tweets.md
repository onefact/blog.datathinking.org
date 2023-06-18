# The Power of Data: Revealing Insights and Pitfalls in Data Analysis - ChatGPT Tweets
### Author: Nesma Mahmoud, Msc of Computer Science 
### Editor: GPT-4

### 📀🤔 Research Question: How does sentiment analysis using different methods impact the classification of sentiment and the identification of sentiment trends?

### 🧐💰 Rationale: 
Sentiment analysis is a widely used technique in various domains, including marketing, social media analysis, and customer feedback analysis. Understanding the sentiment behind textual data can provide valuable insights and inform decision-making processes. However, the accuracy and reliability of sentiment analysis methods are crucial for drawing meaningful conclusions. The research question aims to investigate the impact of using different methods, specifically comparing a flawed method with a pretrained transformer-based method, on sentiment classification and trend analysis.

The rationale behind this question is to highlight the potential pitfalls of relying on inaccurate or flawed sentiment analysis methods. By demonstrating how the misclassification of sentiment can occur and how it can be improved using more advanced techniques like pretrained transformers, the research aims to emphasize the importance of robust and reliable analysis methods.

The decisions regarding which sentiment analysis method to use and how to interpret the sentiment trends will need to be made by the individuals or organizations relying on the analysis results. Researchers, data analysts, marketing professionals, and decision-makers in various industries may be involved in making these decisions.

### 🧐💰 Stakes: The stakeholders who have skin in the game and bear material consequences include:

Researchers and Data Analysts: Their credibility and the validity of their research can be affected by the accuracy of sentiment analysis methods. They may face reputational risks if flawed methods are used, leading to incorrect conclusions or misleading trends.

Marketing Professionals:  analysis plays a crucial role in understanding customer sentiment towards products, brands, and campaigns. If inaccurate  analysis leads to incorrect insights, it can impact marketing strategies, customer engagement, and brand reputation.

Decision-Makers: Managers and executives who rely on data analysis to make informed decisions may face the consequences of inaccurate analysis. Poor decisions based on flawed analysis can lead to financial losses, misaligned strategies, or missed opportunities.

Systems and Platforms: Data analysis techniques are often integrated into various systems and platforms, such as social media monitoring tools or customer feedback analysis platforms. If these systems utilize flawed methods, their users may receive inaccurate data analysis scores and trends, impacting the overall effectiveness and value of the platforms.


### Data Governance: 
Data Usage Policies: Avalilabe for Public use
Ethical Considerations: There is no information provided regarding the ethical considerations taken into account during data collection, such as user consent, privacy protection, or compliance with Twitter's terms of service.
Data Sharing and Sharing Restrictions: The dataset's sharing and redistribution policies are not specified. It is unknown whether there are any restrictions or licenses imposed on the usage or redistribution of the dataset.

### Data Provenance
COLLECTION METHODOLOGY
The tweepy Twitter API is used to extract the Tweets and Authors' data. There are some simple filters applied trying to avoid sensitive tweets and spam as much as possible.

### The Data and What It Represents
Context of the Data: 
The datset is from kaggle: DOI: 10.34740/kaggle/dsv/5685262
The dataset  consists of tweets from the Daily tweets about ChatGPT from Twitter. 

The dataset includes the following columns: [METADATA]
tweet_id: Unique identifier for each tweet.
tweet_created: The date and time when the tweet was created.
tweet_extracted: The date and time when the tweet was extracted or collected.
text: The actual text of the tweet.
lang: The language of the tweet.
user_id: Unique identifier for the user who posted the tweet.
user_name: The name of the user.
user_username: The username/handle of the user.
user_location: The location provided by the user in their profile.
user_description: The description provided by the user in their profile.
user_created: The date when the user account was created.
user_followers_count: The number of followers the user has.
user_following_count: The number of accounts the user is following.
user_tweet_count: The total number of tweets posted by the user.
user_verified: Indicates whether the user account is verified.
source: The source/platform used to post the tweet.
retweet_count: The number of times the tweet was retweeted.
like_count: The number of times the tweet was liked.
reply_count: The number of replies to the tweet.
impression_count: The number of times the tweet was seen.
I created some columns:
cleaned_text: The cleaned version of the tweet text.
sentiment_polarity: The sentiment polarity score of the tweet from poor Sentiment analysis method
sentiment: The sentiment category (positive, negative) assigned to the tweet from poor Sentiment analysis method
date: The formated date extracted from the tweet_created column. 
transformers_sentiment: The sentiment assigned to the tweet using pretrained transformers.
transformers_sentiment_score: The sentiment score assigned by pretrained transformers.
bigram_text: The text with bigrams (pairs of consecutive words) identified.

### Figma Board
Link: https://www.figma.com/file/ceF6KqP9X6c74pxdTf4ZsY/Data-Journey?type=whiteboard&node-id=0%3A1&t=rGCkveaURFVDjG9m-1
<img width="853" alt="image" src="https://github.com/nesmaAlmoazamy/blog.datathinking.org/assets/10960462/f3cdcc30-93e5-4bb8-9415-f554b187656d">

### Mathematics for Sentiment analysis
[math.pdf](https://github.com/nesmaAlmoazamy/blog.datathinking.org/files/11755509/math.pdf)

### Analysis Results

During the analysis of the ChatGPT tweets dataset, an important pitfall of data analysis was identified when using the TextBlob library for sentiment analysis. It was observed that the sentiment analysis results from TextBlob were biased due to the misclassification of neutral sentiments as positive. This raised concerns about the accuracy and reliability of the sentiment analysis performed using this method.

To address this pitfall and improve the sentiment analysis, several steps were taken:

1. Removal of Neutral Sentiments: To mitigate the issue of misclassifying neutral sentiments as positive, a decision was made to remove tweets with neutral sentiments. By considering the sentiment polarity of each tweet, neutral sentiments were identified and excluded from the analysis. This step aimed to ensure a more accurate representation of the positive and negative sentiments within the dataset.

2. Elimination of Duplicate Tweets (Retweets): Another step taken to enhance the data quality was the removal of duplicate tweets, particularly retweets. Duplicate tweets can skew the analysis results and introduce bias, as they provide redundant information. By eliminating retweets, the dataset was streamlined to contain unique tweets, reducing the potential for duplicated sentiments and ensuring data integrity.

3. Leveraging Pretrained Transformers for Sentiment Analysis: To overcome the limitations of the initial flawed sentiment analysis method, pretrained transformers were employed. Transformers, such as BERT or GPT-based models, have demonstrated superior performance in natural language processing tasks, including sentiment analysis. By utilizing the power of these pretrained models, sentiment analysis was performed again on the dataset, yielding more reliable and accurate sentiment classifications. The transformers' ability to capture contextual information and nuances in language contributed to improved sentiment analysis outcomes.

#### By examining the trend of the sentiment analysis using transformers [ Correct Method]

![image](https://github.com/nesmaAlmoazamy/blog.datathinking.org/assets/10960462/4f946087-dcc4-49d1-9046-155f88aac747)

It shows that the negative sentiment count is exceeding the positive counts and that the trend was high at the begining of week 14 and it tends to decrease over time.

#### By examining the trend of the sentiment analysis using TextBlob [ wrong method]

![image](https://github.com/nesmaAlmoazamy/blog.datathinking.org/assets/10960462/cd2caf50-3310-4149-b13d-ba7319921b50)

It shows that the Positive sentiment count is exceeding the negative counts and that the trend for negative sentiment is increasing while the trend for positive sentiment is decreasing over time.

It is crucial to recognize the limitations and pitfalls associated with using flawed sentiment analysis methods, as demonstrated by the disparities between the results obtained from TextBlob and transformers. The incorrect analysis serves as a reminder of the importance of employing reliable and accurate methods, such as pretrained transformers, to obtain meaningful insights from sentiment analysis in text data.

### Visualization:
#### Word Cloud: Unigram Word Cloud:
The unigram word cloud provides insights into the most frequently occurring single words in the dataset. Each word is represented in the word cloud, with larger and bolder fonts indicating higher frequencies. By examining the unigram word cloud, we can identify the prominent words used in the ChatGPT tweets and gain an understanding of the key topics, themes, or sentiments expressed by users.

![image](https://github.com/nesmaAlmoazamy/blog.datathinking.org/assets/10960462/3ec4596a-85a6-4137-a508-5bc1be853a62)

#### Word cloud: Bigram word cloud: 
The bigram word cloud offers insights into pairs of consecutive words that commonly occur together in the dataset. It identifies collocations or phrases that provide more contextual meaning than individual words. By analyzing bigrams, we can identify significant word combinations, expressions, or frequently co-occurring phrases within the tweets.

![image](https://github.com/nesmaAlmoazamy/blog.datathinking.org/assets/10960462/36282e14-84e2-4972-bbb9-17696bdc487e)

### Notebook for replication:
https://github.com/nesmaAlmoazamy/blog.datathinking.org/blob/patch-1/pages/Code:%20The%20Power%20of%20Data:%20Revealing%20Insights%20and%20Pitfalls%20in%20Data%20Analysis%20-%20ChatGPT%20Tweets.ipynb

---

Thanks for reading. Stay tuned for more data-driven stories!
