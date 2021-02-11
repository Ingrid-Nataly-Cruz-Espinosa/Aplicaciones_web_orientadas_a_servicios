import requests
import json

result = result = requests.get("https://www.etnassoft.com/api/v1/get/?id=589&callback=?")

libros = result.json()

items = libros
encoded = json.dumps(items)
decoded = json.loads(encoded)

titulo=str(decoded[0]["title"][0])
print(titulo)
autorlibro=str(decoded[0]["author"][0])
autorlibro.replace("[","")
autorlibro.replace("]","")
print(autorlibro)
contenido=str(decoded[0]["content"])
print(contenido)
publicacion=str(decoded[0]["publisher"])
print(publicacion)
url=str(decoded[0]["url_download"])
print(url)
cover=str(decoded[0]["cover"])
print(cover)
imagen=str(decoded[0]["thumbnail"])
print(libros)





