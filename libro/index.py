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
    
    resultado = requests.get("https://www.etnassoft.com/api/v1/get/?id=589&callback=?q"+bookname)

    libros = resultado.json()

    items = libros["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    titulos=str(decoded[0]["title"])
    autorlibros=str(decoded[0]["author"])
    contenidos=str(decoded[0]["content"])
    publicaciones=str(decoded[0]["publisher"])
    urls=str(decoded[0]["url_download"])
    covers=str(decoded[0]["cover"])
    

    titulo="<label>'"+titulos+"'</label>"
    autorlibro="<label>'"+autorlibros+"'</label>"
    contenido="<label>'"+contenidos+"'</label>"
    publicacion="<label>'"+publicaciones+"'</label>"
    url="<label>'"+urls+"'</label>"
    cover="<label>'"+covers+"'</label>"

    datos={
      
      "bookname":"El nombre del libro es: "+bookname,
      "titulo":titulo,
      "autorlibro":"Autor libro: "+autorlibro,
      "contenido":"Contenido: "+contenido,
      "publicacion":"Fecha de publicacion: "+publicacion
      "ur"
      "url":"¿Quieres adquirir el libro? Da clic en el link: "+link

    }
    return render.index(datos)