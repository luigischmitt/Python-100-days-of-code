import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "my_key"
API_KEY_NEWS = "my_key"
ACCOUNT_SID = "my_key"
AUTH_TOKEN = "my_key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(STOCK_ENDPOINT, params={"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": API_KEY_STOCK})
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]
print(before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

positive_diff = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price))
print(positive_diff)
up_down = None
if positive_diff > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_diff = round((positive_diff / float(yesterday_closing_price)) * 100)
print(percentage_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if abs(percentage_diff) > 1:
    print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(percentage_diff) > 1:
    response2 = requests.get(NEWS_ENDPOINT, params={"apiKey": API_KEY_NEWS, "qInTitle": COMPANY_NAME})
    articles = response2.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_diff}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(ACCOUNT_SID, AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages \
                    .create(
                        body=article,
                        from_="+17075959294",
                        to="my_number"
                    )
    print(message.status)

