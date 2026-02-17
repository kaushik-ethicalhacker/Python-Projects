import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = ""
TOKEN = ""
GRAPH_ID = "trackinggraph"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Running Tracker",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today().strftime("%Y%m%d")

pixela_params = {
    "date":today,
    "quantity":float(input("How many kilometers did you run?\n")),
}

response = requests.post(url=pixela_endpoint, headers=headers, params=pixela_params)
response.raise_for_status()
print(response.text)









update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

