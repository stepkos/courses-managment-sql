import psycopg
from contextlib import contextmanager



@contextmanager
def psql():

    conn = psycopg.connect(f"host={host} port={port} dbname={dbname} user={user} password={password}")

    try:
        yield conn
    finally:
        conn.close()
