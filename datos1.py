from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from crear_tabla import *

from configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos) 


Session = sessionmaker(bind=engine)
session = Session()

# Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 110553
codParroquia = session.query(Establecimiento, Parroquia).join(Parroquia).filter(Parroquia.codigo == "110553").all()

print("_________Consulta 1_________")

for r in codParroquia:
	print(r, ("\n"))
#____________________________________________#
# Todos los establecimientos de la provincia del Oro.
proOro = session.query(Establecimiento, Provincia).join(Provincia).filter(Provincia.nombre == "Oro").all()
print("_________Consulta 2_________")

for p in proOro:
	print(p("\n"))
        
#____________________________________________#
# Todos los establecimientos del cantón de Portovelo.
canPortovelo = session.query(Establecimiento, Canton).join(Canton).filter(Canton.nombre == "Portovelo").all()

print("_________Consulta 3_________")

for m in canPortovelo:
	print(m("\n"))
#____________________________________________#
# Todos los establecimientos del cantón de Zamora.
canZamora = session.query(Establecimiento, Canton).join(Canton).filter(Canton.nombre == "Zamora").all()

print("_________Consulta 4_________")

for n in canZamora:
	print(n("\n"))
