from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from crear_tabla import *

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos) 

Session = sessionmaker(bind=engine)
session = Session()
# Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
jornada = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == 'Matutina y Vespertina').all()
"_________Consulta 1_________"
for j in jornada:
 print(j,("\n"))

#____________________________________________#
# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
num_Es = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.numEstudiantes == 448 , 
    Establecimiento.numEstudiantes == 450,
    Establecimiento.numEstudiantes == 451,
    Establecimiento.numEstudiantes == 454,
    Establecimiento.numEstudiantes == 458,
    Establecimiento.numEstudiantes == 459 )).all()
"_________Consulta 2_________"
for e in num_Es:
 print(e)