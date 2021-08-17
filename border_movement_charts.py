import pandas as pd 
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#read in data
#download from: https://www.stats.govt.nz/assets/Uploads/Provisional-international-travel-statistics/20210217-daily-movements-across-nz-border-Jan-2019-Aug-2021.zip, save 'data' tab as Border_movement_2019_to_present.csv
data = pd.read_csv("Border_movement_2019_to_present.csv", parse_dates=['date'])

#group by date, citizenship status, direction of travel, and sum the total movements on that day
data_w_citizenship = data.groupby(['date', 'citizenship', 'direction_code'])['total_movements'].sum().reset_index()

#create separate DFs for returning citizens and non citizens, in both directions
returning_citizens = data_w_citizenship.loc[(data_w_citizenship["citizenship"] == "NZ") & (data_w_citizenship["direction_code"] == 'A')]
non_citizen_arrivals = data_w_citizenship.loc[(data_w_citizenship["citizenship"] == "non-NZ") & (data_w_citizenship["direction_code"] == 'A')]
non_citizen_departures = data_w_citizenship.loc[(data_w_citizenship["citizenship"] == "non-NZ") & (data_w_citizenship["direction_code"] == 'D')]
departing_citizens = data_w_citizenship.loc[(data_w_citizenship["citizenship"] == "NZ") & (data_w_citizenship["direction_code"] == 'D')]

#assign rolling averages
returning_citizens['rolling_7'] = returning_citizens['total_movements'].rolling(7, min_periods = 1).mean()
non_citizen_arrivals['rolling_7'] = non_citizen_arrivals['total_movements'].rolling(7, min_periods = 1).mean()
departing_citizens['rolling_7'] = departing_citizens['total_movements'].rolling(7, min_periods = 1).mean()
non_citizen_departures['rolling_7'] = non_citizen_departures['total_movements'].rolling(7, min_periods = 1).mean()


#plot citizen and non citizen arrivals
plt.plot( 'date', 'rolling_7', data = non_citizen_arrivals, color='skyblue', linewidth=3, label='Rolling 7-day average')
plt.plot( 'date', 'rolling_7', data = returning_citizens, color='black', linewidth=3, label='Rolling 7-day average')
plt.plot( 'date', 'total_movements', data = non_citizen_arrivals, color='skyblue', linewidth=1, label='Non-citizen arrivals')
plt.plot( 'date', 'total_movements', data = returning_citizens, color='black', linewidth=1, label='Returning citizens')

dtFmt = mdates.DateFormatter('%Y-%b') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

plt.legend()
plt.show()

#plot citizen and non citizen departures
plt.plot( 'date', 'rolling_7', data = non_citizen_departures, color='skyblue', linewidth=3, label='Rolling 7-day average')
plt.plot( 'date', 'rolling_7', data = departing_citizens, color='black', linewidth=3, label='Rolling 7-day average')
plt.plot( 'date', 'total_movements', data = non_citizen_departures, color='skyblue', linewidth=1, label='Non-citizen departures')
plt.plot( 'date', 'total_movements', data = departing_citizens, color='black', linewidth=1, label='Departing citizens')


dtFmt = mdates.DateFormatter('%Y-%b') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

plt.legend()
plt.show()

#plot citizen arrivals and departures
plt.plot( 'date', 'total_movements', data = returning_citizens, color='green', linewidth=0.5, label='Returning citizens')
plt.plot( 'date', 'rolling_7', data = returning_citizens, color='green', linewidth=3, label='Returning citizens')
plt.plot( 'date', 'total_movements', data = departing_citizens, color='palegreen', linewidth=0.5, label='Departing citizens')
plt.plot( 'date', 'rolling_7', data = departing_citizens, color='palegreen', linewidth=3, label='Departing citizens')

dtFmt = mdates.DateFormatter('%Y-%b') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

plt.legend()
plt.show()

#plot non-citizen arrivals and departures
plt.plot( 'date', 'total_movements', data = non_citizen_arrivals, color='blue', linewidth=0.5, label='Non-citizen arrivals')
plt.plot( 'date', 'rolling_7', data = non_citizen_arrivals, color='blue', linewidth=3, label='Non-citizen arrivals')
plt.plot( 'date', 'total_movements', data = non_citizen_departures, color='skyblue', linewidth=0.5, label='Non-citizen departures')
plt.plot( 'date', 'rolling_7', data = non_citizen_departures, color='skyblue', linewidth=3, label='Non-citizen departures')

dtFmt = mdates.DateFormatter('%Y-%b') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

plt.legend()
plt.show()


