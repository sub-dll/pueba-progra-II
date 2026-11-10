from conexion import Session
from modelos import *

def inserta_Libro(titulo, autor, ejemplares_disponibles):
    with Session.begin() as session:
        Libro= Libro(
            titulo = titulo,
            autor = autor,
            ejemplares_disponibles = ejemplares_disponibles
        )
        session.add(Libro)


    print("Libro Registrado")