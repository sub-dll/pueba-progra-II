from sqlalchemy.orm import Session
from conexion import engine
from modelos import Libro
from modelos import Prestamo

def registrar_Libro(estudiante, Libro_id, fecha):
    if not estudiante.strip() or not fecha.strip():
        print("Error: Datos inválidos.")
        return

    with Session(engine) as session:
        with session.begin():
            Libro = session.get(Libro, Libro_id)
            
            if Libro is None:
                print(f"Error: La sala con id {Libro_id} no existe.")
                return
            
            if not Libro.disponible:
                print(f"Error: La sala '{Libro.nombre}' no esta reservable")
                return

            nuevo_Prestamo = Prestamo(estudiante=estudiante, sala_id=Libro_id, fecha=fecha)
            Libro.disponible = False 
            
            session.add(nuevo_Prestamo)
            
    print(f"Libro para '{estudiante}' registrado con éxito.")