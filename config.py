# config.py

import os
from dotenv import load_dotenv

load_dotenv()

BASE_EMPLOYEES = os.getenv("POSTGRES_CONST_BASE_EMPLOYEES")

class Config:
    # PostgreSQL principal
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    # Conexiones adicionales
    SQLALCHEMY_BINDS = {
        # Aquí cambiamos a pymssql en lugar de pyodbc
        'sqlserver': (
            f"mssql+pymssql://{os.getenv('SQLSERVER_USER')}:"
            f"{os.getenv('SQLSERVER_PASSWORD')}@"
            f"{os.getenv('SQLSERVER_HOST')}:1433/"
            f"{os.getenv('SQLSERVER_DB')}"
        ),
        'db3': BASE_EMPLOYEES,
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'yLxqdG0BGUft0Ep')
