import requests
import json

result = requests.get("https://www.googleapis.com/books/v1/volumes?q=sinsajo")

libro = result.json()

items = libro["items"]

encoded = json.dumps(items)
decoded = json.loads(encoded)
print(decoded[0]["volumeInfo"]["authors"])

autor=str(decoded[0]["volumeInfo"]["authors"])
print(autor)
autor.replace("[","")
autor.replace("]","")
print(decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"])


print (result.text)