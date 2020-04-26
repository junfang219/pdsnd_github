#!/usr/bin/env python
# coding: utf-8

# In[51]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list = ['chicago', 'new york city', 'washington']
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print("Hello! Let\'s explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, Washington, or all ?\n')
        if city.lower() not in city_list:
            print('Please enter the right city name')
        else:
            break
   
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to filter the data? January, February, ... , June, or all.\n')
        if month.lower() not in month_list:
            print('Please enter the correct month')
        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day\'s information to you want to get? Monday, Tuesday, ... Sunday, or all. \n')
        if day.lower() not in day_list:
            print('Please enter the correct day')
        else:
            break

    print('-'*40)
    return city, month, day
    print(city, month, day)
get_filters()


# In[52]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': '/Users/junfang/Downloads/data/chicago.csv',
              'new york city': '/Users/junfang/Downloads/data/new_york_city.csv',
              'washington': '/Users/junfang/Downloads/data/washington.csv' }


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month_list.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
    print(df)


# In[181]:


df = load_data('washington', 'january', 'monday')
print(df)


# In[171]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is', most_common_month)
    

    # TO DO: display the most common day of week
    most_common_week = df['day_of_week'].mode()[0]
    print('The most common week is', most_common_week)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[172]:


time_stats(df)


# In[173]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used Start station is', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('The most commonly used End station is', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] + ' and ' + df['End Station']
    print('The most frequent combination of start station and end station is\n', combination.value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[174]:


station_stats(df)


# In[175]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is', df['Trip Duration'].sum()/3600, 'hours')

    # TO DO: display mean travel time
    print('Mean travel time is', df['Trip Duration'].mean()/60, 'minutes')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[176]:


trip_duration_stats(df)


# In[184]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types are\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Counts of gender are\n', df['Gender'].value_counts())
    else:
        print('Gender information is not available')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('The earliest year of birth is', df['Birth Year'].min())
        print('The most recent year of birth is', df['Birth Year'].max())
        print('The most common year of birth is', df['Birth Year'].value_counts().idxmax())
    else:
        print('Birth year information is not avaiable')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[185]:


user_stats(df)


# In[ ]:




