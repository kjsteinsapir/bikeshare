import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower().strip()
        if city in CITY_DATA:
            break
        else:
            print("City not in database")


    # TO DO: get user input for month
    
    while True:
        months = ['january', 'february', 'march', 'april', 'june','all']
        month = input("By which month would you like to filter? Data contains info from the six first months of the year.").lower().strip()
        if month in months:
            break
        else:
            print("Introduce a valid month")

    
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
        day = input("By which day would you like to filter?").lower().strip()
        if day in days:
            break
        else:
            print("Introduce a valid day")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    #Loading data
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data
    df = pd.read_csv(CITY_DATA[city])

    #StartTime is a string. Have to convert it for python to do operations with it
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Creating new columns to filter
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):

    """
    Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
  
    popular_month = df['month'].mode()[0]
    print(f'most common month is: {popular_month}')
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print(f'most common day is: {popular_day}')

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'most common hour is:{popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_startstation=df['Start Station'].mode()[0]
    print(f'most common Start Station is: {most_startstation}')

    # TO DO: display most commonly used end station
    most_endstation=df['End Station'].mode()[0]
    print(f'most common End Station is: {most_endstation}')

    # TO DO: display most frequent combination of start station and end station trip
    most_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(f'The most common trip is from {most_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    print(f'Total travel time is equal to: {total_travel_time}')
    """
    end_time = df['End Time'].sum()
    start_time = df['Start Time'].sum()
    travel_time = end_time-start_time
    print(f'Total travel time: {travel_time}')
    """

    # TO DO: display mean travel time
    average_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    print(f'Average travel time is equal to: {average_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
    else:
        print("No gender data available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        print('\nEarliest year of birth:', earliest_year)
    except KeyError:
        print('\nEarliest year of birth not available.')

    try:
        recent_year = int(df['Birth Year'].max())
        print('Most recent year of birth:', recent_year)
    except KeyError:
        print('Most recent year of birth not available.')

    try:
        popular_year = int(df['Birth Year'].mode()[0])
        print('Most common year of birth:', popular_year)
    except KeyError:
        print('Most common year of birth not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_raw_data(df):

    raw = input('\nWould you like to see the raw data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count : count+5])
            count += 5
            ask = input('Would you like to see the next 5 raws?')
            if ask.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
