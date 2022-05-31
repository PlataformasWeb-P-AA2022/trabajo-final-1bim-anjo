import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_tabla import Provincia, Canton

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('data/Listado_Instituciones_Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)
    cantones = []
    
    for row in reader:
        # sentecia que permite que no se presenten valores repetidos
        if row[5] not in cantones:
            
            cantones.append(row[5])

            id_provincia = session.query(Provincia).filter_by(nombrePro=row[3]).first()
        # creacion de el objeto Ocantones
            Ocantones = Canton(
                nombre=row[5], codigo=row[4], provincia_id=id_provincia.id)
            session.add(Ocantones)
session.commit()
