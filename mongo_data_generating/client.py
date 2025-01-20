from contextlib import contextmanager

from pymongo import MongoClient

from dotenv import load_dotenv

import os

load_dotenv()

BASE_URL = "mongodb://{user}:{password}@{host}:{port}/?directConnection=true"


@contextmanager
def get_client():
    url = BASE_URL.format(
        user=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        host=os.getenv("MONGO_HOST"),
        port=os.getenv("MONGO_PORT")
    )
    with MongoClient(url) as client:
        yield client


if __name__ == "__main__":
    with get_client() as client_:
        print(client_.server_info())
