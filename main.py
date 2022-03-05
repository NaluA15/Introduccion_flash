from flask import Flask, render_template
#render_template=>es para ver lo de las plantillas y esta busca siempre la carpeta template
app=Flask(__name__)

@app.get("/")#ruta de inicio
def inicio():
    #return "<h1>Hola mundo</h1>"
    return render_template("index.html")

@app.get("/contactos")
def listaContactos():
    return render_template("contactos.html")

#@app.get("/contactos/<contactoId>")#quiere decir que es una ruta dinamica
#@app.get("/contactos/contactoId")#quiere decir toca buscarla por esta ruta
@app.get("/contactos/<int:contactoId>")#quiere decir que es una ruta dinamica de enteros nada mas
def EditarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

@app.get("/edad/<int:edadId>")
def Edades(edadId):
    return render_template("edades.html", Eid=edadId)

app.run(debug=True)