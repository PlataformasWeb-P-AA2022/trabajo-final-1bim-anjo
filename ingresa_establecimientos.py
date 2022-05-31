import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_tabla import Establecimiento, Parroquia

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


with open('data/Listado_Instituciones_Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    next(reader)
    parroquia = []

    # Ciclo repetitivo
    for row in reader:
         # sentecia que permite que no se presenten valores repetidos
        num_Estudiantes = int (row[14],base=0)
        num_Docentes = int (row[15],base=0)

        id_p = session.query(Parroquia).filter_by(nombre=row[7]).first()

        # Creación del objeto de tipo establecimiento
        establecimiento = Establecimiento(
             codigoAMIE = row [0], 
             nombreInstitucion = row [1],
              codDistrito = row[8],
              sostenimiento = row[9], 
              tipoEducacion = row[10],
              modalidad = row[11], 
              jornada = row[12],
              acceso = row[13], 
        numEstudiantes = num_Estudiantes, 
        numDocentes = num_Docentes, parroquia = id_p)
        session.add(establecimiento)
session.commit()
