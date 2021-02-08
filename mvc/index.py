import web
import requests
import json

render= web.template.render("mvc/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self)  :
    form=web.input()
    bookname=form.bookname
    
    resultado = requests.get("https://www.googleapis.com/books/v1/volumes?q="+bookname)

    libro = resultado.json()

    items = libro["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    url = decoded[0]["volumeInfo"]["infoLink"]
    linkimagen=decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"]
    nombre_autor=str(decoded[0]["volumeInfo"]["authors"])
    link ="<a target='blank' href='"+url+"'>"+bookname+"</a>"
    
    imagen ="<img src='"+linkimagen+"'/>"
    autor="<label>'"+nombre_autor+"'</label>"

    datos={
      
      "bookname":"El nombre del libro es: "+bookname,
      "imagen":imagen,
      "autor":"Autor: "+autor,
      "url":"¿Quieres adquirir el libro? Da clic en el link: "+link

    }
    return render.index(datos)