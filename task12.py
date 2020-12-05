import  json
x={
    "Name":"John Doe",
    "Age":22,
    "city":"wisconsin",
    "grade": None,
    "result": True,
    "marks1":{"bio":99,"CS":100},
    "marks2":[70,58,99],
    "avg":97.99
}
y=json.dumps(x)
print(y)
print(json.dumps((1,2,3)))
print(json.dumps(list(range(9))))

from pymongo import MongoClient
myclient=MongoClient("mongodb://localhost:27017/") #making connection
db=myclient["ABC"] #database
Collection=db["data"]
with open('D:\\Python Internship\\task12\\data.json') as f:
    file_data=json.load(f)
if isinstance(file_data,list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)