import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_tabla import Parroquia,Canton

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('data/Listado_Instituciones_Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    next(reader)
    parroquia = []

    for row in reader:
        # sentecia que permite que no se presenten valores repetidos
        if row[7] not in parroquia:
            
            parroquia.append(row[7])

            id_p = session.query(Canton).filter_by(nombre=row[5]).first()

            # Creación del objeto de tipo can
            can = Parroquia(
                nombre=row[7], codigo=row[6], canton=id_p)
            session.add(can)
session.commit()