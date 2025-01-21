from contextlib import contextmanager

from pymongo import MongoClient

from dotenv import load_dotenv

import os

load_dotenv()

BASE_URL = "mongodb://{user}:{password}@{host}:{port}/?directConnection=true"


@contextmanager
def mongo_client_ctx():
    url = BASE_URL.format(
        user=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        host=os.getenv("MONGO_HOST"),
        port=os.getenv("MONGO_PORT")
    )
    with MongoClient(url) as client:
        yield client


if __name__ == "__main__":
    with mongo_client_ctx() as client_:
        print(client_.server_info())
