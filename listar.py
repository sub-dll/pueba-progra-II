from sqlalchemy import select
from conexion import Session
from modelos import Libro

def consultar_libros():
    with Session() as session:
        consulta = select(Libro)
        Libro = session.scalars(consulta).all()

        print("\n---------Listado de Libros---------\n")
        if not Libro:
            print("No existen el Libro")
            return
        for Libro in Libro:
            print("-------------------------------------")
            print("ID : ", Libro.id)
            print("Titulo : ", Libro.titulo)
            print("Autor : ", Libro.autor)
            print("Disponibles : ", Libro.ejemplares_disponibles)

        print("------------------------------------------")