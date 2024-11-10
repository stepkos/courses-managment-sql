import psycopg
from dotenv import dotenv_values

values = dotenv_values()
host = values.get("POSGRES_HOST")
port = values.get("POSTGRES_PORT")
password = values.get("POSTGRES_PASSWORD")
dbname = values.get("POSTGRES_DBNAME")
user = values.get("POSTGRES_USER")

print(user, port, user, password)


with psycopg.connect(
    f"host={host} port={port} dbname={dbname} user={user} password={password}"
) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """
        )

        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

        cur.execute("SELECT * FROM test")
        cur.fetchone()

        for record in cur:
            print(record)

        conn.commit()
