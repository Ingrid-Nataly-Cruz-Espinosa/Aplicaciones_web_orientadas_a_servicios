import web
import requests
import json

render= web.template.render("libro/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self)  :
    form=web.input()
    bookname=form.bookname
    resultado = requests.get("https://www.etnassoft.com/api/v1/get/?"+bookname)

    libros = resultado.json()

    items = libros

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    titulo_1=str(decoded[0]["title"])
    autorlibro_1=str(decoded[0]["author"])
    contenido_1=str(decoded[0]["content"])
    publicacion_1=str(decoded[0]["publisher"])
    url_1=str(decoded[0]["url_download"])
    cover_1=str(decoded[0]["cover"])
    imagen_1=str(decoded[0]["thumbnail"])
    
      

    titulo="<label>'"+titulo_1+"'</label>"
    autorlibro="<label>'"+autorlibro_1+"'</label>"
    contenido="<label>'"+contenido_1+"'</label>"
    publicacion="<label>'"+publicacion_1+"'</label>"
    url="<label>'"+url_1+"'</label>"
    cover="<label>'"+cover_1+"'</label>"
    imagen="<img src='"+imagen_1+"'/>"

    datos={
      
      "bookname":"El nombre del libro es: "+bookname,
      "titulo":titulo,
      "autorlibro":"Autor libro: "+autorlibro,
      "contenido":"Contenido: "+contenido,
      "publicacion":"Fecha de publicacion: "+publicacion,
      "url":"¿Quieres adquirir el libro? Da clic en el link: "+url,
      "cover":"cover: "+cover,
      "imagen":imagen
    }
    return render.index(datos)
