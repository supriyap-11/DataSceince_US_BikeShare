#Submission for github

import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }  #reading the city bikeshare data

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("="*40)
    print('\nHello! Let\'s explore some US bikeshare data!!')
    start_graphic = '''
 o__       __o       __o       __o       __o
 ,>/_     _\<,      _\<,      -\<,      _\<_
()`().....()`().....()`().....()`().....()`()

'''
    print(start_graphic)

    city = input("We can analyze New York City, Washington or Chicago. Please choose one city to analyze: ") # user is asked to enter the city to explore the data for the bike shared system
    city = city.lower()

    city_ascii_img = '''
             ===  _
               |__|
              O    O
           ====================
            '''

    while True:  # to manage user input exceptions
        if  city == "chicago" :
            print("Time for a Chicago Bike ride!")
            print(city_ascii_img)
            #print("Chicago")
            break

        if city == "new york" or city == "newyork" or city == "new york city" or city == "newyorkcity" :
            print("Time for a New York Bike ride!")
            print(city_ascii_img)
            #print("New York")
            break

        elif  city == "washington" :
            print("Time for a Washington Bike ride!")
            print(city_ascii_img)
            break

        else:
            print("Sorry! We don't currently support the city : {}\nEnter a city name you want to study the data about from below choices:".format(city))
            print("Chicago")
            print("New York")
            print("Washington")
            print("="*40)
            city= input("Please enter your choice: ")
            city = city.lower()
            


    month_name= input("Would you like to filter the data by month or you want no filter at all? Type January, February .... to filter by that month or type 'all' (without quotes) for no filters\n") #to filter the data by month
    month_name= month_name.lower()

    while True: 
        if month_name not in ['january','february','march', 'april', 'may', 'june', 'july','august','september','october','november','december','all','jan','feb','apr','mar','jun','jul','aug','sep','oct','nov','dec']: 
            print("Sorry, we did not understand the month name you just entered!")
            month_name= input("Do you want data analysis for any specific month? If yes, please enter month name or enter \"all\" (without quotes): ")
            month_name= month_name.lower()
        
        elif month_name in ['july','august','september','october','november','december', 'jul','aug','sep','oct','nov','dec']: #to handle the input for months other than january to june
            print("Sorry! We don't currently support the month: {}".format(month_name))
            month_name= input("Do you want data analysis for any specific month till June? If yes, enter month name or enter \"all\" (without quotes): ")
            month_name= month_name.lower()

        else:
            print("The data is now filtered by the month - {}\n".format(month_name))
            print ("="*40)
            break




    day_of_week= input("Would you like to filter the data by any day of the week or do you want no filter at all? Type  Monday, tuesday .... to filter by that day or type 'all' (without quotes) for no filters: \n")
    day_of_week= day_of_week.lower()
    while True: 
        if day_of_week not in  ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all","mon","tues","wed","thurs","fri","sat","sun","thu"]: #for input other than weekdays or the short names for weekdays
            print("Sorry, we did not understand the day you just entered!")
            day_of_week= input("Would you like to filter the data by any day of the week or do you want no filter at all? Type Monday, tuesday .... to filter by that day or type 'all' (without quotes) for no filters: \n")
            day_of_week= day_of_week.lower()
            

        else:
            print("The data is now filtered by day - {}\n".format(day_of_week))
            print ("="*40)
            break
    
    # mapping dictionary for handling weekdays
    day_mapping_dict = {"mon":"monday",
                    "tue" :"tuesday",
                    "wed":"wednesday",
                    "thurs": "thursday",
                    "thu": "thursday",
                    "fri": "friday",
                    "sat": "saturday",
                    "sun": "sunday" }

    if day_of_week in day_mapping_dict:
        day_of_week = day_mapping_dict[day_of_week] 

    # mapping dictionary for handling month
    month_mapping_dict = {"jan":"january",
                          "feb": "february",
                          "mar": "march",
                          "apr": "april",
                          "jun": "june"}


    if month_name in month_mapping_dict:
        month_name = month_mapping_dict[month_name]
    
    return city, month_name, day_of_week


def get_day_of_week(start_date : str) -> str:
    date= datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    
    weekday_name= date.weekday() 
    week_array= ["monday","tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
    return week_array[int(weekday_name)]

def get_month_from_date(start_date: str) -> str:
    month = start_date.split("-")[1]
    name_array = ["-","january","february","march", "april", "may", "june"]
    return name_array[int(month)]


def load_data(city,input_month,input_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print("Loading Data...............")
    df = pd.read_csv(CITY_DATA[city])

    print("Adding Filters - if any...........")
    for index, row in df.iterrows():
        start_date = row["Start Time"]
        day = get_day_of_week(start_date)
        month = get_month_from_date(start_date)

        df.set_value(index,"day_col",day) 
        df.set_value(index,"month_col",month) 
    
    print(input_day)

    if input_month.lower() != "all":
        df = df.loc[df['month_col'] == input_month]

    if input_day.lower() != "all":
        df = df.loc[df['day_col'] == input_day]


    print("*******Dataset loaded successfully********")
    return df


def popular_travel_time(df):
    pop_month = df['month_col'].mode()[0] #finding poular hour
    pop_weekday = df['day_col'].mode()[0] #finding popular weekday
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    pop_hour = df['hour'].mode()[0]

    return pop_month,pop_weekday,pop_hour

def station_stats(df):
    com_start_st = df['Start Station'].mode().to_string(index = False)
    com_end_st = df['End Station'].mode().to_string(index = False)

    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    com_trip=  df['trip'].mode().to_string(index = False)
    
    return com_start_st, com_end_st, com_trip

    
def trip_duration_stats(df):
    total_travel_time= df['Trip Duration'].sum()
    avg_travel_time= df['Trip Duration'].mean()
    return total_travel_time,avg_travel_time



def user_stats(df):
    '''input - the data frame
    output- count of each user'''

    user_types= df['User Type'].value_counts()
    return user_types

def get_gender(df,city):
    '''input- the data frame
    output- the count of males and females'''

    if city == 'washington':
        print("no user gender info shared")
        return None
    else:
        user_gender= df['Gender'].value_counts()
        return user_gender

def get_birth_year(df,city):
    '''input df
    output- the earliest, most recent and the most common birth year of the users from the data frame'''

    if city == 'washington':
        return None
    else:
        earliest= int(df['Birth Year'].min())
        most_recent= int(df['Birth Year'].max())
        most_common=int(df['Birth Year'].mode())

        return earliest,most_recent,most_common


def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)

        #printing popular month
        print("Printing the most popular travel time...")
        start_time = time.time()
        pop_month,pop_weekday,pop_hour = popular_travel_time(df)
        time_taken = time.time() - start_time
        print('Most Popular Month:', pop_month)
        print('\nMost Popular weekday:', pop_weekday)
        print('\nMost Popular hour:', pop_hour)
        print("\nThat took {} seconds.\n".format(time_taken))

        print("="*40)

        #printing popular stations and trips
        print("Printing the most popular stations and trips...")
        start_time = time.time()
        com_start_st, com_end_st, com_trip= station_stats(df)
        time_taken = time.time() - start_time
        print("Most common Start Station is {}:".format(com_start_st))
        print("Most common End Station is {}:".format(com_end_st))
        print("Most comon Trip from \'start to end station\' is {}".format(com_trip))
        print("That took {} seconds.\n".format(time_taken))
        print("="*40)

        #trip_duration_stats(df)
        print("Printing the most total and average travel time...")
        start_time = time.time()
        total_time_travel, avg_travel_time= trip_duration_stats(df)
        total_hours= int(total_time_travel/3600)
        total_hours_mod= int(total_time_travel%3600)
        total_minutes= int(total_hours_mod/60)
        total_seconds= int(total_hours_mod%60)
        avg_hours= int(avg_travel_time/3600)
        avg_hours_mod= int(avg_travel_time%3600)
        avg_minutes= int(avg_hours_mod/60)
        avg_seconds= int(avg_hours_mod%60)

        time_taken = time.time() - start_time
        print("The total travel time is {} hours, {} minutes and {} seconds ".format(total_hours, total_minutes, total_seconds))
        print("The total travel time is {} hours, {} minutes and {} seconds ".format(avg_hours, avg_minutes, avg_seconds))

        print("That took {} seconds.\n".format(time_taken))
        print("="*40)

        #printing the user_statistics
        print("Printing the user statistics...")
        start_time = time.time()
        user_types = user_stats(df)
        time_taken = time.time() - start_time
        print(user_types)
        print("That took {} seconds.\n".format(time_taken))
        print("="*40)
        
        #prinitng the gender
        print("Printing the gender statistics...")
        start_time = time.time()
        user_gender = get_gender(df,city)
        time_taken = time.time() - start_time
        print(user_gender)
        print("That took {} seconds.\n".format(time_taken))
        print("="*40)


        #calculating the birth date details
        print("To find the youngest, newest and the most common birth years from the data")

        start_time = time.time()
        birth_details = get_birth_year(df,city)
        time_taken = time.time() - start_time

        if birth_details != None:
            earliest,most_recent,most_common = birth_details
            print ("The earliest user birth year is {}. \n The most recent user birth year is {}.\n The most common user birth year is {}. ".format(earliest,most_recent,most_common))
        else:
            print("no user birth year info shared")

        print("That took {} seconds.\n".format(time_taken))
        print("="*40)

        count=0

        while True:
            raw_input =input("Would to like to see the raw data? Enter yes or no: ")

            if raw_input.lower() != 'yes' and raw_input.lower() != 'y':
                break
            
            else:
                print(df[count: count+ 5])
                print("="*40)
                count= count+ 5

        restart = input('\nWould you like to restart? Enter yes or no: ')  #for restarting the whole analysis

        if restart.lower() != 'yes' and restart.lower() != 'y':
            break


if __name__ == "__main__":
  main()


