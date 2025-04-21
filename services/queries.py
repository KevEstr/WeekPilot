# app/services/queries.py

def execute_query(sql, bind_key='sqlserver'):
    """
    Ejecuta una consulta SQL de sólo lectura contra el bind indicado.
    Devuelve una lista de tuplas con los resultados.
    """
    from app.db import db  # 👈 Importación local para evitar el circular import
    engine = db.get_engine(bind=bind_key)
    with engine.connect() as conn:
        result = conn.execute(sql)
        return result.fetchall()

def get_spare_parts():
    sql = """
    SELECT CODIGO, DESCRIPCIO
    FROM MTMERCIA
    WHERE CODLINEA = 'ST'
    """
    rows = execute_query(sql)
    return [{"code": r[0], "description": r[1]} for r in rows]

def get_product_information():
    sql = """
    SELECT DESCRIPCIO, CODIGO
    FROM MTMERCIA
    WHERE (CODLINEA = 'CEL' AND CODGRUPO = 'SEMI')
       OR (CODLINEA = 'CYT' AND CODGRUPO = 'NUE')
    """
    rows = execute_query(sql)
    return [{"DESCRIPCIO": r[0], "CODIGO": r[1]} for r in rows]

def get_spare_name():
    sql = """
    SELECT DESCRIPCIO
    FROM MTMERCIA
    WHERE CODLINEA = 'ST'
    """
    rows = execute_query(sql)
    return [r[0] for r in rows]

def get_sertec():
    sql = """
    SELECT CODIGO
    FROM MTMERCIA
    WHERE CODIGO = 'SERTEC'
    """
    rows = execute_query(sql)
    return [r[0] for r in rows]

def get_technicians():
    sql = """
    SELECT NOMBRE, CODVEN
    FROM Venden 
    WHERE COMENTARIO LIKE '%TECNICO%'
    """
    rows = execute_query(sql)
    return [{"NOMBRE": r[0], "DOCUMENT": r[1]} for r in rows]
