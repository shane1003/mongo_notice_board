from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MongoURI = os.getenv('MONGO_URI')
client = MongoClient(MongoURI)

db = client.board

collection_artice = db["article"]
collection_account = db["account"]