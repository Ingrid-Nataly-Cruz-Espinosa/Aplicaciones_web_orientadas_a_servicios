import web
import json
urls = (
    '/read?', 'Read'
)
edadapi = web.application(urls, globals())

class EDAD:


    def _init_(self):
      pass
        
     
    def GET(self):
        try:
            edades = web.input() 
            nombre = edades.nombre
            dia = int(edades.dia)
            mes = edades.mes
            año = int(edades.año)
            edad = 2021 - año
            datos={}
            datos["Tu nombre es"] = nombre
            datos["dia d¡nacimiento"] = dia
            datos["Mes de nacimiento"] = mes
            datos["Año de nacimiento"] = año
            datos["Tu edad es"] = edad
            texto = open("static/recaudacion.txt","a")
            texto.write("\n")
            texto.write(str(datos))
            texto.close()
            return json.dumps(datos)

        except:
          datos = {}
          datos["ALERTA"] = "Algo esta mal en tus datos"
          return json.dumps(datos)
       
            

if _name_ == "_main_":
  edadapi.run()


