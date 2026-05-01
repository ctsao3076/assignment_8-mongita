from mongita import MongitaClientDisk
import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
client = MongitaClientDisk(os.path.join(BASE_DIR, "mongita_data"))

db = client.bookstore

categories = list(db.category.find())
books = list(db.book.find())

# Remove the internal _id field
for doc in categories:
    doc.pop("_id", None)
for doc in books:
    doc.pop("_id", None)

with open("categories.json", "w") as f:
    json.dump(categories, f, indent=2)

with open("books.json", "w") as f:
    json.dump(books, f, indent=2)

print("Exported categories.json and books.json")
