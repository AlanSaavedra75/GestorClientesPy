from fastapi import FastAPI

app = FastAPI() 

clientes = {}

@app.post("/clientes/{cliente_id}")
def crear_cliente(cliente_id: int, nombre: str):
    clientes[cliente_id] = {"nombre": nombre}
    return {"mensaje": "Cliente creado exitosamente"}

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    if cliente_id in clientes:
        return clientes[cliente_id]
    return {"error": "Cliente no encontrado"}

@app.put("/clientes/{cliente_id}")
def modificar_cliente(cliente_id: int, nombre: str):
    if cliente_id in clientes:
        clientes[cliente_id]["nombre"] = nombre
        return {"mensaje": "Cliente actualizado"}
    return {"error": "Cliente no encontrado"}

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    if cliente_id in clientes:
        del clientes[cliente_id]
        return {"mensaje": "Cliente eliminado"}
    return {"error": "Cliente no encontrado"}

@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la API de Gestión de Clientes!"}
