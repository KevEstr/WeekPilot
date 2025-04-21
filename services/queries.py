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
    sql = """
    SELECT CODIGO, DESCRIPCIO
    FROM MTMERCIA
    WHERE CODLINEA = 'ST'
    """
    rows = execute_query(sql)
    return [{"code": row[0], "description": row[1]} for row in rows]


def get_product_information():
    sql = """
    SELECT DESCRIPCIO, CODIGO
    FROM MTMERCIA
    WHERE (CODLINEA = 'CEL' AND CODGRUPO = 'SEMI')
       OR (CODLINEA = 'CYT' AND CODGRUPO = 'NUE')
    """
    rows = execute_query(sql)
    return [{"DESCRIPCIO": row[0], "CODIGO": row[1]} for row in rows]


def get_spare_name():
    sql = """
    SELECT DESCRIPCIO
    FROM MTMERCIA
    WHERE CODLINEA = 'ST'
    """
    rows = execute_query(sql)
    return [row[0] for row in rows]


def get_sertec():
    sql = """
    SELECT CODIGO
    FROM MTMERCIA
    WHERE CODIGO = 'SERTEC'
    """
    rows = execute_query(sql)
    return [row[0] for row in rows]


def get_technicians():
    sql = """
    SELECT NOMBRE, CODVEN
    FROM Venden 
    WHERE COMENTARIO LIKE '%TECNICO%'
    """
    rows = execute_query(sql)
    return [{"NOMBRE": row[0], "DOCUMENT": row[1]} for row in rows]
