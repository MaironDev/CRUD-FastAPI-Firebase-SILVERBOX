from db import db
from fastapi import FastAPI, HTTPException
from models import User




users = db.collection(u'users')


app = FastAPI(title="CRUD FastAPI Firebase" , description="FastAPI Firebase prueba SILVERBOX", version="0.1")

@app.get(path="/")
async def root():
    return {"message": "Hello World"}



#OBTENER TODOS LOS USUARIOS
@app.get(path="/users")
async def getUsers():
   
    usersRef = users.get()  # obtenemos los usuarios de la coleccion
    
    usersJson = {} #creamos un diccionario para retornalos como un json
    
    for user in usersRef: #recorremos la coleccion
        usersJson[user.id] = user.to_dict() # agregamos cada usuario  al diccionario
    
    return usersJson


# #AGREGAR UN USUARIO
@app.post(path="/addUser")
async def addUser(user: User):  
    
    userAdd = users.document(f'{user.id}') #instanciamos y añadimos id como llave
    userAdd.set({   #añadimos los datos del usuario
         u'nombre': user.name, 
         u'apellido': user.lastName,
         u'edad': user.age
    })
    return {'status' : 200 , 'message' : 'Usuario Agregado con Exito '}


#ACTUALIZAR UN USUARIO
@app.put(path="/updateUser/{id}")
async def updateUser(id: str, user: User):

    userUpdate = users.document(id)

    userUpdate.update({
        u'nombre': user.name,
        u'apellido': user.lastName,
        u'edad': user.age
    })
    return {'status' : 200 , 'message' : 'Usuario Actualizado con Exito '}


#ELIMINAR UN USUARIO
@app.delete(path="/deleteUser/{id}")
async def deleteUser(id: str):
    userDelete = users.document(id)
    userDelete.delete()

    return {'status' : 200 , 'message' : 'Usuario Eliminado con Exito '}