from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def find_documents(collection: Collection, query: Dict) -> List[Dict]:
    documents = collection.find(query)
    return list(documents)


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "books"
    collection_name = "science_books"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    # Read (Query) Operation
    query = {"name": "John Doe"}
    results = find_documents(collection, query)
    print("Matching documents:")
    for result in results:
        print(result)
