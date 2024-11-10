import psycopg
from contextlib import contextmanager

from data_generating import config


@contextmanager
def postgres_client():

    conn = psycopg.connect(
        f"host={config.POSTGRES_HOST} "
        f"port={config.POSTGRES_PORT} "
        f"dbname={config.POSTGRES_PASSWORD} "
        f"user={config.POSTGRES_DBNAME} "
        f"password={config.POSTGRES_USER}"
    )

    try:
        yield conn
    finally:
        conn.close()
