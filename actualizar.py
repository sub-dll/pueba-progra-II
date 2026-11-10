from conexion import Session
from modelos import Libro

def actualizar_libro(in_id_Libro, in_titulo, in_autor, in_ejemplares_disponibles):
    with Session.begin() as session:
        #Buscar producto con ID
        Libro = session.get(Libro, in_id_Libro)

        if Libro is None:
            print("Libro roducto no encontrado")
            return

        #Actualizar los atributos
        Libro.nombre = in_titulo
        Libro.precio = in_autor
        Libro.stock = in_ejemplares_disponibles

    print("Libro actulizado")