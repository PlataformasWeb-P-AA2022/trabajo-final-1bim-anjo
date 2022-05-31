from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigoPro = Column(String(100))
    nombrePro = Column(String(100))
    # Mapea la relación entre las clases
    # Club puede acceder a los jugadores asociados
    # por la llave foránea
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigoPro=%s nombrePro=%s " % (
            self.codigoPro,
            self.nombrePro)


class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100), nullable=False)
     # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    provincia = relationship("Provincia", back_populates="cantones")
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: codigo: %s - nombre: %s" % (
            self.codigo,
            self.nombre)

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100), nullable=False)
    # se agrega la columna  ForeignKey

    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Mapea la relación entre las clases
    canton = relationship("Canton", back_populates="parroquia")
    establecimiento = relationship(
        "Establecimiento", back_populates="parroquia")

    def __repr__(self):
        return "Parroquia: codigo:%s - nombre: %s - IdCanton: %s"  % (
            self.codigo,
            self.nombre,
            self.canton_id)



class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigoAMIE = Column(String(100))
    nombreInstitucion = Column(String(100))
    codDistrito = Column(String(50))
    sostenimiento = Column(String(100))
    tipoEducacion = Column(String(100))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    numEstudiantes = Column(Integer)
    numDocentes = Column(Integer)
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # Mapea la relación entre las clases
    parroquia = relationship("Parroquia", back_populates="establecimiento")

    def __repr__(self):
        return "Establecimiento: codigoAMIE=%s - nombreInstitucion=%s - codDistrito=%s - sostenimiento=%s - tipoEducacion=%s - modalidad=%s - jornada=%s - acceso=%s - numEstudiantes=%d - numDocentes=%d " % (
            self.codigoAMIE,
            self.nombreInstitucion,
            self.codDistrito,
            self.sostenimiento,
            self.tipoEducacion,
            self.modalidad,
            self.jornada,
            self.acceso,
            self.numEstudiantes,
            self.numDocentes)

Base.metadata.create_all(engine)
