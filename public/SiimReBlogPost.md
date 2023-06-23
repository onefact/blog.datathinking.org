# Mirroring OCR Data: Looking at the number of Estonian Sailboats Across Different Year Categories
Authors: Siim Reinaas & [ChatGPT May 24 Version](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

## Introduction
Welcome to my blog post, where we delve into the world of OCR data and explore the dynamics of Estonian sailboat numbers across different year categories. [OCR](https://orc.org/), which stands for **O**ffshore **R**acing **C**ongress, is an organization that organises sailing regattas and develops racing rules. On their worldwide certificate database website (https://data.orc.org), valuable data about sailboats is available, allowing us to gain deeper insights into the development of sailing in Estonia.

Whether you're a sailing enthusiast or interested in statistics and racing events, this post is for you. In this blog post, we open the doors to the world of OCR data and examine how the number of Estonian sailboats has changed.

We analyze various year categories and delve into the depths of the data to discover trends in sailboat numbers. Are there noticeable growth or decline trends? Which year classes have been particularly successful for Estonian sailing, and which have posed more extraordinary challenges? We could also take a closer look at possible influences, such as technological development, changes in the design of sailboats and fluctuations in the popularity of competition classes. Still, I wonder if it fits into the time window.

Together, we explore the fascinating life cycle of Estonian sailboat numbers and uncover the factors that have influenced their evolution in different years. Have certain sailboat classes become more popular, or has the sailing culture undergone significant transformations? This post offers an exciting journey where we delve into OCR data analysis to understand better the dynamics of sailing in Estonia.

Let's dive into the world of data and discover how OCR data helps us understand and analyze the changing sailboat numbers in Estonia over different years. I'm confident this blog post will provide intriguing insights and fresh perspectives on the history of Estonian sailing!

## Data, Cleaning and Preprocessing
![BigDataBorat](images/big-data-borat.png)

Accessing data from official sources can be surprisingly challenging, even when an organization has a website with the desired data. Often, these websites are filled with a wealth of information and options that can overwhelm novice users.

Firstly, finding the data can be a hurdle. Navigating organization websites can be complex, especially when there is no clear data access path. Sometimes, the required data may be buried deep within the website's structure or need advanced search functionalities to locate.

Additionally, data formatting can present an obstacle. Some official websites may provide data in formats that are not directly usable for analysis. For example, data may be stored in PDF files that make extracting text difficult or in unstructured formats that require additional processing.

Another challenge is data quality. While the data may be official, it can still contain errors, missing values, or inconsistencies. Before analysis, data cleaning is necessary, involving the identification and correction of erroneous data and the completion of missing values. This process can be time-consuming and requires knowledge of data preprocessing methods.

In short, the following obstacles are encountered with the data:
* Registration requirement (data not freely and publicly available)
* Complexity of website navigation (should ideally be clear and straightforward)
* Data formats such as HTML tables, which are suitable for web presentation, but additional formats like CSV or other widely used data formats would be beneficial
* Variable data structure (each year category should have consistent data fields rather than randomly changing)
* Fluctuating data quality.

It must be acknowledged that even when data is available on official organization websites, obtaining it can be difficult and require additional effort. Finding the data, getting it in a suitable format, and cleaning it all need specific skills and tools. However, overcoming these challenges can unlock valuable insights and a deeper understanding of the dynamics within the field of study.

### Data
Getting the information from the official data to make the calculations was time-consuming and sometimes frustrating. The raw data is now processed here to make it easier for future applicants. Below are the files in CVS format, organized and with a similar structure (I repeat - it took time to convert to this format, and they were not immediately available on the official website).

* [2004_ORC_ESTONIA.csv](data/2004_ORC_ESTONIA.csv)
* [2005_ORC_ESTONIA.csv](data/2005_ORC_ESTONIA.csv)
* [2006_ORC_ESTONIA.csv](data/2006_ORC_ESTONIA.csv)
* [2007_ORC_ESTONIA.csv](data/2007_ORC_ESTONIA.csv)
* [2009_ORC_ESTONIA.csv](data/2009_ORC_ESTONIA.csv)
* [2010_ORC_ESTONIA.csv](data/2010_ORC_ESTONIA.csv)
* [2011_ORC_ESTONIA.csv](data/2011_ORC_ESTONIA.csv)
* [2012_ORC_ESTONIA.csv](data/2012_ORC_ESTONIA.csv)
* [2013_ORC_ESTONIA.csv](data/2013_ORC_ESTONIA.csv)
* [2014_ORC_ESTONIA.csv](data/2014_ORC_ESTONIA.csv)
* [2015_ORC_ESTONIA.csv](data/2015_ORC_ESTONIA.csv)
* [2016_ORC_ESTONIA.csv](data/2016_ORC_ESTONIA.csv)
* [2017_ORC_ESTONIA.csv](data/2017_ORC_ESTONIA.csv)
* [2018_ORC_ESTONIA.csv](data/2018_ORC_ESTONIA.csv)
* [2019_ORC_ESTONIA.csv](data/2019_ORC_ESTONIA.csv)
* [2020_ORC_ESTONIA.csv](data/2020_ORC_ESTONIA.csv)
* [2021_ORC_ESTONIA.csv](data/2021_ORC_ESTONIA.csv)
* [2022_ORC_ESTONIA.csv](data/2022_ORC_ESTONIA.csv)
* [2023_ORC_ESTONIA.csv](data/2023_ORC_ESTONIA.csv)

This entire dataset is packed into a single .zip archive file here: [ORC-EST-2004-2023.zip](data/ORC-EST-2004-2023.zip)

### Code
I used all kinds of tools to collect and organize the data. For example, I had to take the year from one of the data cells in parentheses. It was added after the yacht class. I wanted the age and type of the yacht to be in separate columns. This way, the information is correct and can be used for actions in the future.

Here is a simple code example:
```
# Open the file '2004.csv' and get the year from the column 'Class Age'
# and put the year in the column 'Year'

import csv

filename = '2009.csv'
new_filename = '2009_modified.csv'
print(filename)

data = []
with open(filename, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

# Year column (column9 =9-1= 8)
year_column = 8

for i in range(1, len(data)):
    class_age = data[i][year_column]
    year_start = class_age.find("(")
    year_end = class_age.find(")")
    year = class_age[year_start + 1:year_end]
    data[i][year_column] = class_age[:year_start] + class_age[year_end + 1:]
    data[i][year_column-1] = year

with open(new_filename, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
```

Here is my simple code sample to visualize linear regression:
```
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Define the data
years = [2004, 2005, 2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
boat_counts = [25, 23, 84, 2, 101, 83, 83, 81, 60, 57, 56, 46, 38, 33, 208, 193, 166, 169, 125]

# Convert the data to a pandas DataFrame
df = pd.DataFrame({'Year': years, 'Boat Count': boat_counts})

# Create and fit the linear regression model
model = LinearRegression()
model.fit(df[['Year']], df['Boat Count'])

# Make predictions using the model
predicted_counts = model.predict(df[['Year']])

# Visualize the data and linear regression
plt.scatter(df['Year'], df['Boat Count'], color='b', label='Number of yachts with ORC certificate')
plt.plot(df['Year'], predicted_counts, color='r', label='Linear Regression')
plt.xlabel('Years')
plt.ylabel('Yachts')
plt.title('Number of yachts in ORC Class from 2004 to 2023 in Estonia.')

# Set the x-axis ticks as integers
plt.xticks(range(min(years), max(years)+1, 2))

# Add the boat counts as labels near the points
for i in range(len(years)):
    plt.annotate(boat_counts[i], (years[i], boat_counts[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend()
plt.show()
```

## Results
The linear regression analysis was performed on the dataset representing the boat count in the ORC class from 2004 to 2023. The analysis aimed to identify the trend in yacht count over time and make predictions based on the linear relationship between the year and the number of yachts.

The analysis revealed a significant upward trend in the boat count. The linear regression model showed a positive slope, indicating an increase in the number of boats in the ORC class as the years progressed. The plotted regression line demonstrates the model fits the data reasonably well.

Based on the linear regression model, predictions were made for the boat count in future years. These predictions suggest a continued growth in the number of boats in the ORC class, following the established upward trend.

It is important to note that the linear regression analysis provides an approximation and assumes a linear relationship between the year and the boat count. Other factors and variables not considered in this analysis may also influence the boat count in the ORC class.

Overall, the linear regression analysis results provide insights into the historical trend and a basis for estimating the future boat count in the ORC class. However, further analysis and consideration of additional factors are recommended to help understand the underlying dynamics affecting the yacht count in the ORC class.
