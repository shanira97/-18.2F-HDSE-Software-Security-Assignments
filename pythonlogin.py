import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["usertbl"]

uname = input("Enter user name : ")
pword = input("Enter password : ")
for x in collection.find({},{"u_name":1,"pwd":1}):
	name = str(x["u_name"])
	password=str(x["pwd"])
if uname==name and pword==password:
	print("login successful")
else:
	print("login failed")