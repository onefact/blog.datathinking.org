--- 
title: Gender-Based Analysis of Tartu Bike Sharing Service
authors: Indrek Romet

---

# {% $markdoc.frontmatter.title %}

Authors: {% $markdoc.frontmatter.authors %}
Editor: {% $markdoc.frontmatter.editor %}

[Edit this page](https://github.com/onefact/blog.datathinking.org/edit/main/pages/understanding-3-1-1-service-requests.md)

A bike-sharing service was launched in Tarth in 2019. The usage patterns of this system in Tartu, especially in comparison with other cities, are not fully known.

## The Data 

Every ride taken in the bike sharing system is recorded. Among the recorded information points, some relvant ones are:

- The first digits of a users Personal Id Code, which represent the gender
- The location, date and time of taking out the bike, and and where and when it was dropped off
- The type of bicyle used (electric or  regular)
- And other less useful information!

This data can allow us learn more about trends and patterns in the gender of Tartu SmartBike users

## Raw Research: How many users of each gender

An approximately 60-40 split between males and females

## But what about during the winter?

The 'Created Date' and 'Closed Date' fields can tell us a lot about how responsive the city is to these service requests. By calculating the difference between these dates, we can measure the efficiency of each agency and even identify patterns that might be affecting performance.

## Location, Location, Location

With 'Incident Zip' and 'Borough' fields, we can plot service requests geographically. This visualization can highlight areas with high service demand or places where certain types of complaints are more prevalent. This information is invaluable for city planners and policymakers.

## Wrapping Up

The data from 3-1-1 service requests tells a story that goes beyond mere numbers. It's a narrative about the city's responsiveness, its challenges, and its ongoing journey to improve the lives of its residents. As we continue to analyze this data, we can help create a more responsive and efficient city.

---

Thanks for reading. Stay tuned for more data-driven stories!
