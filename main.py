import os
import pandas as pd
import datetime as dt
import glob as glob
from random import choice
import smtplib



#-----------------------------------------------------------------------------------
MY_EMAIL = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
#------------------------------- Functions -----------------------------------------
def get_random_letter():
    """returns a random birthday letter"""
    file_list = glob.glob('./letter_templates/*.txt')
    random_birthday_wish = choice(file_list)
    with open(random_birthday_wish, 'r') as letter:
        return letter.read()

def send_birthday_letter(letter, e_mail):
    """sends birthday letter email"""
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=e_mail,
                            msg= f"Subject: Happy Birthday\n\n{letter}")

#--------------------------------------------------------------------------------------
# get today's day and month for comparison
now = dt.datetime.now()
birthday_month = now.month
birthday_day = now.day

#load up the dataframe from the csv file
birthday_df = pd.read_csv('birthdays.csv')

#loop through the dataframe for anyone whose birthday matches today's month and day
birthday_people = [{"name": str(row["name"]).title(),"email":row["email"]} for index, row in birthday_df.iterrows()
                   if row.month == birthday_month and row.day == birthday_day]

#loop through the list of people with birthdays today and send letter
#yes, I could have done this from the for loop above, but it seemed
#easier to have a collection of all who had a birthday
for dic in birthday_people:
    birthday_letter = get_random_letter()
    letter_text = birthday_letter.replace("[NAME]", dic["name"])
    send_birthday_letter(letter_text, dic["email"])

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




