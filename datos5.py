from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ ,desc

from crear_tabla import *

from configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores
ordNumEs = session.query(Establecimiento).filter(Establecimiento.numDocentes > 100).order_by(
	desc(Establecimiento.numEstudiantes)).all()
print("_________Consulta 1_________")

for c in ordNumEs:
	print(c,("\n"))

#___________________________________#
# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores
ordNumDoc = session.query(Establecimiento).filter(Establecimiento.numDocentes > 100).order_by(
		desc(Establecimiento.numDocentes)).all()
print("_________Consulta 2_________")

for d in ordNumDoc:
	print(d,("\n"))