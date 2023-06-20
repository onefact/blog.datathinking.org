--- 
title: Gender-Based Analysis of Tartu Bike Sharing Service
authors: Indrek Romet
coauthor: ChatGPT

---

# {% $markdoc.frontmatter.title %}

Authors: {% $markdoc.frontmatter.authors %}
Editor: {% $markdoc.frontmatter.editor %}


A bike-sharing service was launched in Tarth in 2019. The usage patterns of this system in Tartu, especially in comparison with other cities, are not fully known. Data from Australia, UK and Canada show women use bikes at rates of only 21%,  29% and 30% respectively, while in Germany, Denmark and the Netherlands 40% or more of the rides are by females (Pucher & Buehler, 2008). This blog post analyzes differences in bike usage between males and females in Tartu based on 2022 bike-sharing usage data. 


## The Data 

Every ride taken in the bike sharing system is recorded (https://geohub.tartulv.ee & https://ratas.tartu.ee/). Among the recorded information points, some relvant ones are:

- The first digits of a users Personal Id Code, which represent the gender. And odd number is for female, and an even one is male. (https://learn.microsoft.com/en-us/microsoft-365/compliance/sit-defn-estonia-personal-identification-code?view=o365-worldwide)
- The location, date and time of taking out the bike, and and where and when it was dropped off
- The type of bicyle used (electric or  regular)
- And other less useful information!

This data can allow us learn more about trends and patterns in the gender of Tartu SmartBike users

After downloading the CSV files with all the monthly bike rides, I combined the files into one, as can be seen in the example code snippet below:

![Alt Text](files/CodeSnippet1.png)

## Raw Research: How many users of each gender

An approximately 60-40 split between males and females. This is close to other bike friendly countries in Europe, an encouraging sign.

![Alt Text](files/visualization(19).png)

And here is a population pyramid of the users over the warmer half of the year (as well as the part of the year with full bicycle availability)

![Alt Text](files/CodeSnippet1.png)

## But what about during the winter?

The split is closer to 70-30, male to female respectively, in the winter.

![Alt Text](files/visualization(18).png)

## WHy is that, are the bikes to blame?

There are no electric bikes offered during the winter months. Could the precentages between genders be greatly changed because of a lack of electric bikes offered? Looking at the preference in the summer months, when both types of bikes are fully available, we see that there is difference between bicycle preference. This would lead to inconclusive evidence on what drive this difference in demographics. 

![Alt Text](files/visualization(23).png)

And the population pyramid. Note: older age group too!

![Alt Text](files/visual20).png)

## While we're here, can we predict the length of a trip based on age and gender?

Absolutely not, totally pointless, but worth the try.

![Alt Text](files/codesnippet3.png)

Here is the formula for linear regression:

![Alt Text](files/svg1.svg)

And in our case specifically:

![Alt Text](files/svg2.svg)

## Conclusion and sources

The data from the Tartu SmartBike usage shows that the share of bike use between genders is similar to other European bike-friendly nations. However, this share changes in the winter months. 

---

Thank you reading :)