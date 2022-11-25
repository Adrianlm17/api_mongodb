# We import the libraries indicated by the MongoDB API
import requests
import json


# We ask the minimum value that the user wants to spend on a bike
priceBikeMin = input("Indicates the minimum range that you want to spend on a bike: ")

# We ask the maximum value that the user wants to spend on a bike
priceBikeMax = input("Indicates the maximum range you want to spend on a bike: ")


# We import the MongoDB API and tell it to show us all the bikes that are between the price range indicated by the user
url = "https://data.mongodb-api.com/app/data-ljzmf/endpoint/data/v1/action/find"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes_api",
    "dataSource": "Cluster0",
    "filter": {
         "price": {
            "$gt": priceBikeMin,
            "$lt" : priceBikeMax
         }
    }
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ca2GscUTzJFkllznSlly1cQjc4HJYZKHrVWy6AJExJ6AkbUrKcJcaAaYPSdozho6", 
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)