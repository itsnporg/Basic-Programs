import requests
from datetime import datetime


USERNAME = "yourusername"
TOKEN = "addtokenxd"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

#setting up user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "GRAPH_ID",
    "name": "Articles",
    "unit": "day",
    "type": "float",
    "color": "shibafu",
}


# mandiatory to use header for secure auth
headers = {
    "X-USER-TOKEN": TOKEN,

}
# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)


# pixelcreation
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()

pixel_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("how many articles have you written today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)   
# 


# delete_endpoint = update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


