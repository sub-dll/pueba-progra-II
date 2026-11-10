from decimal import Decimal
from sqlalchemy import String, Numeric, Integer, CheckConstraint, Columnfrom, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date

class Base(DeclarativeBase):
    pass

class Libro(Base):
    __tablename__ = 'Libro'
    __table_args__ = (
        CheckConstraint("precio >=0", name="ck_precio"),
        CheckConstraint("ejemplares_disponibles >=0", name="ck_ejemplares_disponibles")
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    autor: Mapped[str] = mapped_column(String(100), nullable=False)
    ejemplares_disponibles: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self):
        return (f"Libro (id={self.id}, titulo={self.titulo!r})>,"
                f"autor={self.autor}, ejemplares_disponibles={self.ejemplares_disponibles})")
        
        
        
class Usuario(Base):
    __tablename__ = 'Usuario'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return (f"Usuario (id={self.id}, nombre={self.nombre!r})>,"
                f"correo={self.correo}")
      
      
      
       
class Prestamo(Base):
    __tablename__ = 'Prestamo'
    __table_args__= (
        CheckConstraint('cantidad > 0')
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    libro_id: Mapped[int] = mapped_column(ForeignKey("Libro.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("Usuario.id"))
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[int] = mapped_column(bool, nullable=False)

    def __repr__(self):
        return (f"Prestamo (id={self.id}, libro_id (id={self.libro_id})>,"
                f"usuario_id={self.usuario_id}, cantidad={self.cantidad}, estado={self.estado})")





