from contextlib import contextmanager

import psycopg

from data_generating import config


@contextmanager
def postgres_client():

    conn = psycopg.connect(
        f"host={config.POSTGRES_HOST} "
        f"port={config.POSTGRES_PORT} "
        f"dbname={config.POSTGRES_DBNAME} "
        f"user={config.POSTGRES_USER} "
        f"password={config.POSTGRES_PASSWORD}"
    )

    try:
        yield conn
    finally:
        conn.close()
