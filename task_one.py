# pylint: disable= missing-docstring
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
from typing import Dict, Any


class DatabaseControl:
    def __init__(
        self, host: str, port: int, db_name: str, collection: Collection
    ) -> None:
        self.client = MongoClient(host, port)
        self.database = self.client[db_name]
        self.collection = self.database[collection]

    def add_book(self, book_obj: Dict[str, Any]):
        book = self.collection.insert_one(book_obj)
        return book.inserted_id

    def get_book_by_id(self, book_id: str):
        objInstance = ObjectId(book_id)
        return self.collection.find_one({"_id": objInstance})

    def update_book(self, book_id: str, update: Dict[str, Any]):
        result = self.collection.update_many(
            {"_id": ObjectId(book_id)}, {"$set": update}
        )
        return result.modified_count

    def delete_book(self, book_id: str):
        objInstance = ObjectId(book_id)
        result = self.collection.delete_many({"_id": objInstance})
        return result


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "books"
    collection_name = "science_books"

    editor = DatabaseControl(mongodb_host, mongodb_port, database_name, collection_name)

    add_book = {
        "name": "Parašyta krauju",
        "author": "Chris Carter",
        "ISBN": 9786094902000,
        "price": 15.59,
    }
    # editor.add_book(add_book)
    # print(editor.get_book_by_id(book_id="645d2aeb2c0b72f0117ae5eb"))
    # editor.update_book("645d2cb342fe47f9c687ac96", {"price": 20.99})
    # print(editor.get_book_by_id("645d2cb342fe47f9c687ac96"))
    editor.delete_book("645d2cb342fe47f9c687ac96")

    # Connect to MongoDB
    # db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    # collection = db[collection_name]

    # Read (Query) Operation
    # query = {"name": "John Doe"}
    # results = find_documents(collection, query)
    # print("Matching documents:")
    # for result in results:
    #     print(result)
