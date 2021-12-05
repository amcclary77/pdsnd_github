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
        try:
            city = input("Please enter chicago, new york city, or washington: ")
            city=city.lower()
            if city in ['chicago', 'new york city', 'washington']:
                print('Thank you!')
                break
        except:
            #else:
                print('Oops, that city isn\'t valid for this program. Please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please enter a month that\'s in the first half of the year or enter all: ')
            month = month.lower()
            #print(month)
            if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                print('Thank you for your input.')
            break
        except:
        #else:
            print('Hmmm, looks like you entered an invalid month. Please try again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Please enter any day of the week or all: ')
            day = day.lower()
            #print(day)
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' 'all']:
                print('Thank you for that.')
                break
        except:
        #else:
            print('Something went wrong. Check for spelling errors and try again.')
        finally:
            print('-'*40)
            return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    #print(df.head())
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df['Start Time'].head())

    df['month'] = df['Start Time'].dt.month
    #print(df['month'].head())
    df['day'] = df['Start Time'].dt.day_name()
    #print(df['day'].head())

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        #print(df['month'].head())


    if day != 'all':
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        df = df[df['day'] == day.title()]
        #print(df['day'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_dow = df['day'].mode()[0]
    print('The most common day of week is: ', common_dow)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', start_station)
    print()
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', end_station)
    print()
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combo = df['Start Station'] + " " + "and" + " " + df['End Station'].mode()[0]
    frequent_combo = frequent_combo.max()
    print('The most frequent combination of start and end stations is: ', frequent_combo)
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', travel_time)
    print()
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel)
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
    # TO DO: Display counts of user types
        user_type_cnt = df.groupby(['User Type']).sum()
        print('User Type Count: \n', user_type_cnt)

    # TO DO: Display counts of gender
        gender_cnt = df.groupby(['Gender']).sum()
        print('Gender Count: \n', gender_cnt)

        #print(df['Gender'])
    # TO DO: Display earliest, most recent, and most common year of birth

        e_birthyear = df['Birth Year'].min()
        print('The earliest year of birth is: ', e_birthyear.astype(int))
        print()

        r_birthyear = df['Birth Year'].max()
        print('The most recent year of birth is: ', r_birthyear.astype(int))
        print()

        c_birthyear = df['Birth Year'].mode()[0]
        print('The most common year of birth: ', c_birthyear.astype(int))
        print()

    except KeyError:
        print()
        print('There is no additional data available for Washington.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc=0
        while True:
            if view_data == 'yes':
                print(df[start_loc:5])
                start_loc +=5
                view_data = input('Do you wish to continue?: ').lower()
                start_loc +=5
            else:
                if view_data == 'no':
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
