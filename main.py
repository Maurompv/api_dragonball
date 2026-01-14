from fastapi import FastAPI

app = FastAPI()

# Nuestra base de datos de los Guerreros Z
guerreros_z = [
    {
        "id": 1, 
        "nombre": "Goku", 
        "raza": "Saiyajin", 
        "fases": ["Base", "SSJ", "SSJ3", "Ultra Instinto"]
    },
    {
        "id": 2, 
        "nombre": "Vegeta", 
        "raza": "Saiyajin", 
        "fases": ["Base", "SSJ", "Majin", "Ultra Ego"]
    },
    {
        "id": 3, 
        "nombre": "Gohan", 
        "raza": "Hibrido", 
        "fases": ["Base", "SSJ", "SSJ2", "Modo Bestia"]
    },
    {
        "id": 4, 
        "nombre": "Trunks", 
        "raza": "Hibrido", 
        "fases": ["Base", "SSJ", "Super Trunks", "Rage"]
    }
]

# 1. Endpoint de bienvenida
@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la API de Dragon Ball Z! 🐉"}

# 2. Endpoint para ver a todos los personajes
@app.get("/personajes")
def obtener_personajes():
    return guerreros_z