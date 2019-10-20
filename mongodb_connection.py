import pymongo
myclinet = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclinet["database1"]
mycol = mydb["new_customers"]
mylist = [{ "name":"John","address":"Highway 37"}, {"name": "Hannah", "address": "Mountain 21"}]
# mylist = [{"name":"John","address":"Highway 37"}, { "name": "Hannah", "address": "Mountain 21"}]
my_dict = {'name' : 'Superman' , 'address' :'US'}
mycol.delete_many({})

# mycol.delete_many(my_dict)
# try:	
# x = mycol.insert_many(mylist)
# except Exception as ex:	
	# print('Yeahhhhh')
	# template = "An exception of type {0} occurred. Arguments:\n{1!r}"
	# message = template.format(type(ex).__name__, ex.args)
	# print(message)
mycol.insert_one(my_dict)
# below is 'Advanced query' used to find out all the names starting with letter 'S' in the table.

# my_query = { 'name' : {"$gt":"S"}}

# below is 'Regular expression query' used to find out all the names starting with letter 'S' in the table.

# my_query = {'name' : {'$regex':'^S'}}

# updating a document in the collection.  

# myquery = {'name' : {'$regex' : '^S'}}
# set = {'$set' : {'address' : ' Jamaica'}}

# mycol.update_many(myquery,set)

# print(x.inserted_ids)
	
# inserting single element in 'customers' table
# print(myclinet.list_database_names())
# val = mycol.find(my_query)
# lists all the databases in the connection 'myclinet'
all_databases = myclinet.list_database_names()
# if 'database1' in all_databases:
	# print('The database exists')
# print(x._id)
# for x in mycol.find():
	# print(x)
# for x in val:
	# print(x)
print('nn',mycol.find_one())
# Using sort function to sort the data, first parameter is a the key name through which you want to sort the data, second argument is for direction, by deafult it is ascending.
# you can sort the data '-1' for desending, and '1' for ascending.
# sorted_data = mycol.find({},{'address':1}).sort('name', -1)
for x in mycol.find({'address':'US'}):
	print(x)
result = mycol.create_index([('user_ids', pymongo.ASCENDING)], unique=True)
print(sorted(list(mycol.index_information())))

# for x in mycol.find(my_dict):
	# print(x)