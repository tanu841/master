from pymongo import MongoClient
client=MongoClient("mongodb+srv://admin:admin1234@cluster0.xrmp1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.todo_db
collection_name=db["todo_collection"]
