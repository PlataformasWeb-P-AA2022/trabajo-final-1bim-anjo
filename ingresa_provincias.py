from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_tabla import Provincia, Canton

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
provincias = []

with open('data/Listado_Instituciones_Educativas.csv', 'r', encoding="utf8") as archivo:
   
    for r in archivo:
        r = r.split('|')
        provincias.append((r[2], r[3]))

    for p in provincias:
        session.add(Provincia(codigoPro=p[0], nombrePro=p[1]))

session.commit()
