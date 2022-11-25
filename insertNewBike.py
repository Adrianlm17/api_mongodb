import requests
import json

# We ask the user their characteristics
nameBike = input("Write the name of the new bike: ")
typeBike = input("What kind of bike is it: ")
priceBike = input("What price does it have: ")

# We import the MongoDB API and tell it the new bike to add
url = "https://data.mongodb-api.com/app/data-ljzmf/endpoint/data/v1/action/insertOne"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes_api",
    "dataSource": "Cluster0",
    "document":{
       "name": nameBike,
       "type": typeBike,
       "price": priceBike
    }
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ca2GscUTzJFkllznSlly1cQjc4HJYZKHrVWy6AJExJ6AkbUrKcJcaAaYPSdozho6",
}

response = requests.request("POST", url, headers=headers, data=payload,)
print(response.text)