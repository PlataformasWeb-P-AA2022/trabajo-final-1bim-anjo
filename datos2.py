from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from crear_tabla import *

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos) 


Session = sessionmaker(bind=engine)
session = Session()

jornada = session.query(Parroquia, Establecimiento).join(Establecimiento).filter(and_(Establecimiento.modalidad == "Matutina y Vespertina")).all()

print("Consulta 1")

for j in jornada:
 print(j)

#____________________________________________#
num_Es =  session.query(Canton, Establecimiento).join(Establecimiento).filter(or_(Establecimiento.numEstudiantes == "448", Establecimiento.numEstudiantes == "450", Establecimiento.numEstudiantes == "451", Establecimiento.numEstudiantes == "454", Establecimiento.numEstudiantes == "458", Establecimiento.numEstudiantes == "459")).all()

print("Consulta 2")

for e in num_Es:
 print(e)