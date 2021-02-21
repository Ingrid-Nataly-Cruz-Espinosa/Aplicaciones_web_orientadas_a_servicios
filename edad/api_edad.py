import web
import json
urls = (
    '/read?', 'api_edad'
)
app = web.application(urls, globals())

class api_edad:


    def _init_(self):
      pass
        
     
    def GET(self):
        try:
            edades = web.input() 
            nombre = edades.nombre
            dia = int(edades.dia)
            mes = edades.mes
            nacimiento = int(edades.nacimiento)
            edad = 2021 - nacimiento
            informacion={}
            informacion["Tu nombre es"] = nombre
            informacion["dia nacimiento"] = dia
            informacion["Mes de nacimiento"] = mes
            informacion["Año de nacimiento"] = nacimiento
            informacion["Tu edad es"] = edad
            texto = open("static/recaudacion.txt","a")
            texto.write("\n")
            texto.write(str(informacion))
            texto.close()
            return json.dumps(informacion)

        except:
          informacion = {}
          informacion["ALERTA"] = "Algo esta mal en tus informacion"
          return json.dumps(informacion)
       
            

if __name__ == "__main__":

  app.run()


