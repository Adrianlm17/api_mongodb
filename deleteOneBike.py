# We import the libraries indicated by the MongoDB API
import requests
import json


# We ask the user which Bike ID they want to delete
idBike = input("Write the ID of the bike you want to delete: ")


# We import the MongoDB API and tell it to delete the bike that the user has indicated to us
url = "https://data.mongodb-api.com/app/data-ljzmf/endpoint/data/v1/action/deleteOne"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes_api",
    "dataSource": "Cluster0",
    "filter": { "_id": { "$oid": idBike } }
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ca2GscUTzJFkllznSlly1cQjc4HJYZKHrVWy6AJExJ6AkbUrKcJcaAaYPSdozho6", 
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
