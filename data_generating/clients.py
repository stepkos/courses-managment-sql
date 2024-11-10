import psycopg
from contextlib import contextmanager
from dotenv import dotenv_values

@contextmanager
def psql():
    values = dotenv_values()
    host = values.get("POSGRES_HOST")
    port = values.get("POSTGRES_PORT")
    password = values.get("POSTGRES_PASSWORD")
    dbname = values.get("POSTGRES_DBNAME")
    user = values.get("POSTGRES_USER")

    conn = psycopg.connect( f"host={host} port={port} dbname={dbname} user={user} password={password}")

    try:
        yield conn
    finally:
        conn.close()
