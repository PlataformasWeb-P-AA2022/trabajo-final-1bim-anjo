from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from crear_tabla import *

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)
 

Session = sessionmaker(bind=engine)
session = Session()
# Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
numPro = session.query(Canton).join(Parroquia, Establecimiento).filter(
     Establecimiento.numDocentes == 0 and
     Establecimiento.numDocentes == 5 and 
     Establecimiento.numDocentes == 11).all()
print("_________Consulta 1_________")

for n in numPro:
 print(n,("\n"))

#____________________________________________#

# Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
parrPindal = session.query(Establecimiento).join(Parroquia).filter(and_
    (Parroquia.nombre == "PINDAL",
    Establecimiento.numEstudiantes >= 21)).all()
print("_________Consulta 2_________")

for e in parrPindal:
 print(e,("\n"))