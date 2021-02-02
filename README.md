# Data Engineer NanoDegree: Capstone Project

## Project Summary

How to handle immigration is a serious concern for any country, whenever trying to understand this phenomenon some questions arise, like: How to better support people comming into the country? Are cultural differences to be aware of? How this people could better integrate in our society? Decision makers would need reliable and fast information to find solution to these issues

The projects goal is to consolidate the different data sources to expand the US I94 immigration data with extended data such as US demographics, temperature and US airport data, all of that using a Extract, Transform and Load process, all of that in order to create an analytics database using a star schema. This could help to get accurate information from multiple separated sources and allow decision makers to establish sensible policies to tackle the issues described above

## Clearly state the rationale for the choice of tools and technologies for the project.

Pandas is the tool used to ease the data preprocessing and visualisation. Is a very efficient load and manipulation data tool. At a later stage, instead of pandas dataframes, Spark dataframes should be used, this to allow distributed processing is even possible to use for example Amazon Elastic Map Reduce (EMR). To perform automated updates, an ETL pipeline should be integrated into an Airflow DAG. 

A Jupyter Notebook was used to show the data structure and also to design and execute operations like the data cleaning step. Python is a powerful language for data processing, and Jupyter notebooks is a very intuitive and flexible environment to test and execute data operations.

## Propose how often the data should be updated and why. 

According to the data sample the I94 immigration data set is being aggregated each month. So probably updating the data on the same interval is a reasonable approach.

## Write a description of how you would approach the problem differently under the following scenarios:
 
 1. **The data was increased by 100x.**
 - One alternative is to use Spark to process the data efficiently in a distributed way for example with AWS Elastic Map Reduce.
 
 2. **The data populates a dashboard that must be updated on a daily basis by 7am every day.**
 - It is worth consider using Airflow to schedule and automate the data pipeline jobs. Built-in retry and monitoring mechanism that can fullfill this requirement.
 
 3. **The database needed to be accessed by 100+ people.**
 - We could scale up using the same estructure but with cloud infraestructure this time or use RedShift to provide high availability and allow multiple accesses.