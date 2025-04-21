# services/queries.py

from extensions import db
from sqlalchemy import text


def execute_query(sql: str, bind_key: str = 'sqlserver'):
    """
    Ejecuta una consulta SQL de solo lectura contra el bind indicado.
    Devuelve una lista de tuplas con los resultados.
    """
    # Obtener el engine asociado al bind
    engine = db.get_engine(bind=bind_key)

    # Ejecutar la consulta con un context manager
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
