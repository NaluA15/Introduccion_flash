from flask import Flask, flash, render_template, request, redirect, url_for
#render_template=>es para ver lo de las plantillas y esta busca siempre la carpeta template
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="productos"
)
db.autocommit = True

app=Flask(__name__)
app.secret_key = '##91!IyAj#FqkZ2C'

@app.get("/")#ruta de inicio
def inicio():
    cursor = db.cursor(dictionary=True)#Abrir cursor-- ahi se va a mostrar como diccionario
    cursor.execute("select * from productos")#Ejecutar una consulta
    productos = cursor.fetchall()#Obtener todo lo de la consulta en la variable "productos"
    #productos = cursor.fetchone()#Trae el primer dato de la consulta
    #print(productos)
    #print(productos[5]["nombre"])#poker


    cursor.close()#Cerrar cursor
    #return "<h1>Hola mundo</h1>"


    return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

#======================================================PRODUCTOS===================================================================
@app.post("/form_crear")
def crearProducto():
    #Recuperar los datos del formulario 
    nombre = request.form.get('nombre')
    price = request.form.get('price')

    #validar 
    is_valid=True

    if nombre=="":
        flash("El nombre es requerido")
        is_valid=False

    if price=='':
        flash("El precio es requerido")
        is_valid=False

    if not price.isdigit():
        flash("El precio debe ser número")
        is_valid=False

    if not is_valid:#is_valid==False
        return render_template('crearProducto.html', nombre=nombre,price=price,)

    #Insertar los daos en la base de datos
    cursor = db.cursor()
    cursor.execute("insert into productos(nombre, price) values(%s, %s)", (
        nombre,
        price,
    ))
    cursor.close()
    #Volver al listado
    return redirect(url_for('inicio'))

@app.route("/eliminar/<int:id>")
def eliminarProducto(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE id = {0}".format(id))
    cursor.close()
    return redirect(url_for('inicio'))

@app.get("/form_editar")
def formEditarProducto():
    return render_template('editarProducto.html')

@app.route('/editarProducto/<int:id>', methods = ['POST', 'GET'])
def editarProducto(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = {0}".format(id))
    item = cursor.fetchall()
    cursor.close()
    return render_template('editarProducto.html', producto = item[0])

@app.route('/actualizarProducto/<id>', methods=['POST'])
def actualizarProducto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        price = request.form['precio']
        cursor = db.cursor()
        cursor.execute("UPDATE productos SET  nombre = %s, price = %s WHERE id = %s", (nombre, price, id)) 
        return redirect(url_for('inicio'))
#=======================================================================================================================================

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