# We import the libraries indicated by the MongoDB API
import requests
import json


# We import the MongoDB API and configure it to show us all the content we have in the database
url = "https://data.mongodb-api.com/app/data-ljzmf/endpoint/data/v1/action/find"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes_api",
    "dataSource": "Cluster0",
    "filter": {
        
    }
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ca2GscUTzJFkllznSlly1cQjc4HJYZKHrVWy6AJExJ6AkbUrKcJcaAaYPSdozho6", 
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)