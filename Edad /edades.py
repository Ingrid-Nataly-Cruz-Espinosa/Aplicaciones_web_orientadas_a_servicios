import web
import json

urls=(
  "/read?", "Read"
)
def GET(self):
  try:
    data = web.input()
    nombre = data.nombre
    dia = int(data.dia)
    mes = data.mes
    año = int(data.año)
    años = 2021 - años