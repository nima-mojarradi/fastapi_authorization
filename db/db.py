# import asyncio
# import logging
# from pymongo.errors import ServerSelectionTimeoutError
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# async def async_mongo_connect():
#     try:
#         uri = "mongodb+srv://nimamojarradi83:<password>@cluster0.q2jko4j.mongodb.net/?retryWrites=true&w=majority"
#         client = MongoClient(uri, server_api=ServerApi('1'))
#         db = client['library']
#         books_table = db['books']
#         users_table = db['users']
        
#         await asyncio.sleep(1)
#         await client.admin.command('ping')
#         print("Pinged your deployment. You successfully connected to MongoDB!")

#     except ServerSelectionTimeoutError as e:
#         logging.error("Server selection timeout error: %s", str(e))
#         print(f"Unable to connect to the database. Reason: {str(e)}")
#     except Exception as e:
#         logging.error("Exception: %s", str(e))
#         print(f"Unexpected error: {str(e)}")

# asyncio.run(async_mongo_connect())



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb://localhost:27017"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('podcast_manager')
users_collection = db.get_collection('users')
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)