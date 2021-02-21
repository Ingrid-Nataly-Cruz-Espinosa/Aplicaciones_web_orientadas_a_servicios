import web
import json
urls = (
    '/edad?', 'Edad'
)
app = web.application(urls, globals())
class Edad():
    def _init_(self): 
        pass
    def GET(self):  
        try:
            parameter = web.input() 
            name = parameter.name
            day = int(parameter.day)
            month = parameter.month
            year = int(parameter.year)
            age = 2021 - year
            dato={}
            dato["name"] = name
            dato["day"] = day
            dato["month"] = month
            dato["year"] = year
            dato["age"] = age
            archivo = open("static/recaudacion.txt","a")
            archivo.write(str(dato))
            archivo.close()
            return json.dumps(dato)
        except:
            data ={}
            data["error"] = "error 404 la url no existe"
            return data
if _name_ =="_main_": #
    app.run


