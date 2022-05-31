from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, desc

from crear_tabla import *

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
  
# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
esOrdenados = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.numDocentes > 40 , Establecimiento.tipoEducacion.like("%Educación regular%"))).order_by(desc(Parroquia.nombre)).all()
print("_________Consulta 1_________")

for e in esOrdenados:
	print(e,("\n"))
#____________________________________________#
# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.
esCod = session.query(Establecimiento).filter(Establecimiento.codDistrito == "11D04").order_by(desc(Establecimiento.sostenimiento)).all()
print("_________Consulta 2_________")

for c in esCod:
	print(c,("\n"))