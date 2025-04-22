# services/queries.py

from extensions import db
from sqlalchemy import text, create_engine


engine = create_engine(
    'mssql+pymssql://db_read:mHRL_%3C%3D%27%28%5D%2C%23aZ%29T%22A3QeD@20.109.21.246:1433/MICELU',
    echo=False,
    pool_pre_ping=True
)

def execute_query(sql: str):
    """
    Ejecuta una consulta SQL de solo lectura usando el engine inline.
    Devuelve lista de tuplas.
    """
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        return result.fetchall()

def get_spare_parts():
    query = '''
    SELECT CODIGO, DESCRIPCIO
    FROM MTMERCIA
    WHERE CODLINEA = 'ST'
    '''
    results = execute_query(query)
    spare_parts = []
    for row in results:
        spare_parts.append({
            "code": row[0],
            "description": row[1]
        })
    return spare_parts


def get_product_information():
    query = '''
    SELECT DESCRIPCIO, CODIGO
    FROM MTMERCIA
    WHERE (CODLINEA = 'CEL' AND CODGRUPO = 'SEMI') OR (CODLINEA = 'CYT' AND CODGRUPO = 'NUE')
    '''
    results = execute_query(query)
    information = []
    for row in results:
        information.append({
            "DESCRIPCIO": row[0],
            "CODIGO": row[1],
        })
    return information


def get_spare_name():
    query = '''
    SELECT DESCRIPCIO
    FROM MTMERCIA
    WHERE CODLINEA = 'ST'
    '''
    results = execute_query(query)
    spare_names = []
    for row in results:
        spare_names.append(row[0])
    return spare_names


def get_sertec():
    query = '''
    SELECT CODIGO
    FROM MTMERCIA
    WHERE CODIGO = 'SERTEC'
    '''
    results = execute_query(query)
    sertec_values = []
    for row in results:
        sertec_values.append(row[0])
    return sertec_values


def get_technicians():
    query = """
    SELECT NOMBRE, CODVEN
    FROM Venden 
    WHERE COMENTARIO LIKE '%TECNICO%' 
    """
    results = execute_query(query)
    technicians = []
    for row in results:
        technicians.append({
            "NOMBRE": row[0],
            "DOCUMENT": row[1]
        })
    return technicians
