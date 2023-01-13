The goal of this project is to analyze and explore correlations and trends derived from VALORANT match data. There are roughly 1.1 million recorded matches being used for analysis. The code for the webscraper used is in the Web Scraping directory of this project and performs a breadth-first-search approach to adding user matches to a MySQL DB. A mixture of machine learning and exploratory analysis is being conducted on this data. 

The main question being asked about this data is if we can use machine learning to determine if a user is a Smurf or not. A Smurf is a term used to describe a person who intentionally plays a competetive video game at a lower skill level than their own to gain an advantage. 


Questions:

Ideas:
    -Outliers for kills/damage didnt have much to infer about, but splitting players with large rank increases could be interesting. 