import smtplib
import datetime as dt
import random

MY_EMAIL = "testerluigi22@gmail.com"
MY_PASSWORD = "lzmmqkwzjmknlone"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open(file="Python-100-days-of-code/day 32 -  Intermediate+/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL, 
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )





