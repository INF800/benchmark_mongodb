import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)