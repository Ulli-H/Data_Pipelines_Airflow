# Data_Pipelines_Airflow
Data pipelines in Airflow


*An Udacity Data Engineer Nanodegree project*

## Content
- [Description](#description)
- [Data](#data)
- [Pipeline](#Pipeline)
- [Redshift](#Redshift)
- [Links](#links)



## Description  

The subject of the project is the fictional music streaming provider "Sparkify", which is in need of an automated ETL pipeline for their data warehouse. In order to meet the clients needs, Apache Airflow is chosen to do the job. 



## Data  

The data used for this project consists of a song dataset and log dataset, which are both stored in s3 buckets. Both datasets are multiple files in JSON format. 
The song data files are partitioned by the first 3 letters of each song's track ID and contain information on each song and the artist of the song. 

The logdata files contain event data for every event of user activity that happended in the app during one day. The files are partitioned by year and date. 

All data was provided by Udacity as part of the data engineer nanodegree. 



## Pipeline
The pipeline consists out of the following steps:
1. Extract data from S3 locations
2. Load data into staging tables in Redshift
3. Transform data into fact and dimension tables
4. Perform data quality check



## Redshift DWH  

The database is named "sparkifydb" and consists out of the following tables:

#### - staging table for events data:
A staging table for the log dataset. 

#### - staging table for songs data:
A staging table for the song dataset.


#### - fact table: songplays (records in the log data associated with song plays)  
columns: *songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

#### - dimension table: users (data on app users)  
columns: *user_id, first_name, last_name, gender, level*

#### - dimension table: songs (data on all songs in library/app)  
columns: *song_id, title, artist_id, year, duration*

#### - dimension table: artists (data on all artists in library/app)  
columns: *artist_id, name, location, latitude, longitude*

#### - dimension table: time (timestamps of songplays in log data brocken down in different units)  
columns: *start_time, hour, day, week, month, year, weekday*



## Links

[Repository](https://github.com/Ulli-H/Data_Pipelines_Airflow)  
