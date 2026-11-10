from conexion import Session
from modelos import Libro

def eliminar_Libro(in_id_Libro):
    with Session.begin() as session:
        Libro = session.get(Libro, in_id_Libro)

        if Libro is None:
            print("Libro no encontrado")
            return
        
        session.delete(Libro)


    print("Libro eliminado")