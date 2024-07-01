
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
dt=pd.read_csv(r'C:\\Users\\lenovo\\Downloads\\Summer-Olympic-medals.csv',encoding='ISO-8859-1')
# print the dataset
print(dt.head())
#1.data cleaning and preparation
#check the shape of the data (found 15433 rows and 11 columns using eda).
print(dt.shape)
#description of the dataset like mean value ,median,count,std,max,min etc using eda
print(dt.describe())
#check all columns in this data using eda(city,year,sports,discipline,event,athlete,gender,country_code,country,event_gender,medal)
print(dt.columns)
#check for unique values 
print(dt.nunique())
#check for seperate columns unique values using column names
print(dt['Gender'].unique())
#identify mising values or check for null values 
print(dt.isnull().sum())
# handling missing values
dt.dropna(inplace=True)
print(dt)
dt['Year'] = dt['Year'].astype(int)
print(dt.astype)
print(dt.dtypes)

#2.exploratory data analysis 
#a.Conduct initial explorations to understand the distribution of medals, 
#number of participating nations, and other key metrics.(EDA)
medal_counts = dt['Medal'].value_counts()
print(medal_counts)
num_country = dt['Event'].nunique()
print(f'Number of participating event: {num_country}')
#b.Visualize the overall trends in data, such as total medals won over the years.(EDA)
total_medals_year = dt.groupby('Year').size().reset_index(name='total_medals')
print(total_medals_year)
#3.Country-Level Performance Analysis:
#a.Analyze the performance of countries over the years in terms of medals won.
medals_by_country_year = dt.groupby(['Country', 'Year','Medal']).size().reset_index(name='medal_count')
print(medals_by_country_year.head())
#top 10 countries with total medals
total_medals_by_country = dt.groupby('Country').size().reset_index(name='total_medals').sort_values(by='total_medals', ascending=False)
print(total_medals_by_country.head(10)) 

#4.Athlete Performance Metrics:
#a.Evaluate the achievements of athletes, identifying standout performers and their medal hauls.
medals_by_athlete = dt.groupby('Athlete').size().reset_index(name='total_medals').sort_values(by='total_medals', ascending=False)
print(medals_by_athlete.head(20))

medals_by_athlete_type = dt.pivot_table(index='Athlete', columns='Medal', aggfunc='size', fill_value=0)
print(medals_by_athlete_type.head(10))

top_athletes = medals_by_athlete.merge(medals_by_athlete_type, on='Athlete')
print(top_athletes.head(10))

medals_by_gender = dt.groupby('Gender').size().reset_index(name='total_medals').sort_values(by='total_medals', ascending=False)
print(medals_by_gender)

#5.Sport and Event-Specific Trends:
#a.Break down the analysis by individual sports and events to identify trends and dominant nations in each.
sp = 'Swimming'
sport_s = dt[dt['Sport'] == sp]
medals_years = sport_s.groupby('Year').size()
#print(f"Total medals over the years for {sports}:")
print(medals_years)
# Dominant countries in the given sport
medals_by_nation = sport_s.groupby('Country').size().sort_values(ascending=False)
#print(f"Top nations in {Sport}:")
print(medals_by_nation.head(10))
print("\n")
#6.a)Analyze changes in sports disciplines over the years, including the introduction or removal of sports from the Olympics.


    


#8.Data Visualization and Reporting:
#a.Create dynamic visualizations and dashboards that allow stakeholders to interact with
#the data and extract personalized insights.
# Create a line plot showing the number of sports per year
'''sports_per_year = sport_presence.sum(axis=1)
plt.figure(figsize=(14, 6))
plt.plot(sports_per_year.index, sports_per_year.values, marker='o')
plt.title('Number of Sports Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Sports')
plt.grid(True)
print(plt.show())'''






