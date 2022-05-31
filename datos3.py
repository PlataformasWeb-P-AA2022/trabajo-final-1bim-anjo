from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from crear_tabla import *

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)
 

Session = sessionmaker(bind=engine)
session = Session()

numPro =  session.query(Canton, Establecimiento).join(Establecimiento).filter(or_(Establecimiento.numDocentes == "0", Establecimiento.numDocentes == "5", Establecimiento.numDocentes == "11")).all()

print("Consulta 1")

for n in numPro:
 print(n)

#____________________________________________#

parrPindal = session.query(Establecimiento, Parroquia).join(Parroquia).filter(and_(Establecimiento.numEstudiantes >= "21", Parroquia.nombre == "Pindal")).all()

print("Consulta 2")

for e in parrPindal:
 print(e)