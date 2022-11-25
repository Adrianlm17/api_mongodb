# We import the libraries indicated by the MongoDB API
import requests
import json


# We show the types of bikes we have and ask the user which one they want to see
typeBike = input("These are the types of bikes we have:\n 1 - MTB\n 2 - City\n 3 - Electric\n What kind of bike do you want to see?")


# We import the MongoDB API and tell it to show us the type of bike that the user has indicated
url = "https://data.mongodb-api.com/app/data-ljzmf/endpoint/data/v1/action/find"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes_api",
    "dataSource": "Cluster0",
    "filter": {
        "type": typeBike
    }
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ca2GscUTzJFkllznSlly1cQjc4HJYZKHrVWy6AJExJ6AkbUrKcJcaAaYPSdozho6", 
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)