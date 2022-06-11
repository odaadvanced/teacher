# Write your code here :-)
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["memlok"]

print(myclient.list_database_names())
collist = mydb.list_collection_names()
if "users" in collist:
  print("The collection exists.")

mycol = mydb['users']

#myquery = {{ "userId": { "$gt": "S" }},{"userId": 1}}

mydoc = mycol.find( {"userId": { "$lt": "b" }},{"email":1,"_id":0})

for x in mydoc:
  print(x)
