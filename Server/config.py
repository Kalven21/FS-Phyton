import pymongo
import certifi

con_str="mongodb+srv://zamorakevin21:DontForget21@107-ch46.foamavi.mongodb.net/?retryWrites=true&w=majority&appName=107-ch46"

client = pymongo.MongoClient(con_str,tlsCAfile=certifi.where())
db = client.get_database("107-ch46")
