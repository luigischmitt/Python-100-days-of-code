import requests
from datetime import datetime

USERNAME = "my_username"
TOKEN = "my_token"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Duolingo Graph",
    "unit": "day",
    "type": "int",
    "color": "shibafu"
}

headers = {"X-USER-TOKEN": TOKEN}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

post_endpoint = f"{graph_endpoint}/graph1"

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

post_update = {
    "quantity": "5",
}

update_endpoint = f"{post_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.put(url=update_endpoint, json=post_update, headers=headers)
# print(response.text)

delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

