# We import the libraries indicated by the MongoDB API
import requests
import json


# We ask the user which bike he wants to modify its price
idModifyBike = input("Select the ID of the bike you want to modify the price: ")
newPrice = input("Indicates the new price of the bike: ")


# We import the MongoDB API and tell it to modify the price of the bike indicated by the user:
url = "https://data.mongodb-api.com/app/data-ljzmf/endpoint/data/v1/action/updateOne"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes_api",
    "dataSource": "Cluster0",
    "filter": { "_id": { "$oid": idModifyBike } },
      "update": {
          "$set": {
              "price": newPrice
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
