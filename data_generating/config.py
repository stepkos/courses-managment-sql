from dotenv import dotenv_values

envs = dotenv_values()

POSTGRES_HOST = envs.get("POSTGRES_HOST")
POSTGRES_PORT = envs.get("POSTGRES_PORT")
POSTGRES_PASSWORD = envs.get("POSTGRES_PASSWORD")
POSTGRES_DBNAME = envs.get("POSTGRES_DBNAME")
POSTGRES_USER = envs.get("POSTGRES_USER")
