from flask import Flask, render_template, request, redirect, url_for
import mysql.connector #conector de base de datos
#render_template=>es para ver lo de las plantillas y esta busca siempre la carpeta template

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3306,
    database='productos'  ,  
)

db.autocommit = True

app=Flask(__name__)

@app.get("/")#ruta de inicio
def inicio():
    cursor= db.cursor(dictionary=True)

    cursor.execute("select * from productos")
    producto = cursor.fetchall() #obtener todo lo de la consulta
    #producto = cursor.fetcheone() #obtener un solo registro
    print(producto)
    print(producto[5]['nombre']) #poker


    cursor.close()
    #return "<h1>Hola mundo</h1>"
    return render_template("index.html", productos=producto)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProductos.html")

@app.post("/form_crear")
def crearProducto():
    #recuperar los datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')

    #insertar los datos en la base de datos
    cursor = db.cursor()

    cursor.execute("insert into productos(nombre, price) values(%s,%s)",(
        nombre,
        price,
    ))

    cursor.close()

    return redirect(url_for('inicio'))

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