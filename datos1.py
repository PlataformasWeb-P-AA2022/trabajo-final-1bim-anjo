from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from crear_tabla import *

from configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos) 


Session = sessionmaker(bind=engine)
session = Session()

codParroquia = session.query(Establecimiento, Parroquia).join(Parroquia).filter(Parroquia.codigo == "110553").all()

print("Consulta 1")

for r in codParroquia:
	print(r)
#____________________________________________#
proOro = session.query(Establecimiento, Provincia).join(Provincia).filter(Provincia.nombre == "Oro").all()

print("Consulta 2")

for p in proOro:
	print(p)
        
#____________________________________________#
canPortovelo = session.query(Establecimiento, Canton).join(Canton).filter(Canton.nombre == "Portovelo").all()

print("Consulta 3")

for m in canPortovelo:
	print(m)
#____________________________________________#
canZamora = session.query(Establecimiento, Canton).join(Canton).filter(Canton.nombre == "Zamora").all()

print("Consulta 4")

for n in canZamora:
	print(n)
