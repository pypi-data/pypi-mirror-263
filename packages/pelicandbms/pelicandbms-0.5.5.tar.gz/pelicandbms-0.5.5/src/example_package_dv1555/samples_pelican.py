import pickle
from pelicandb import Pelican,DBSession,feed
import os
from pathlib import Path
import os
import time

import sys
import gc
import queue
import threading

def check_name(document, value):
    if document.get("name")== value:
        return True
    else:
        return False
    
def check_document_before_change(type,document):
    
    if document == None:
        raise ValueError("Document is null")
    else:
        if isinstance(document, list):
            document.append({"Checked":True})  
        else:
            document['Checked'] = True

q = queue.Queue()


db = Pelican("samples_db55",path=os.path.dirname(Path(__file__).parent),RAM = False, queue=q, singleton=True)


db["goods2"].register_before_change_handler(check_document_before_change)
id = db["goods2"].insert([{"name1":"Банан","_id":"111222"}], upsert=True)


dbmap = {"samples_db5":db}

res1 = db['goods_1'].find({"name":"banana"})
res2 = db['goods_1'].find([check_name,"banana"])





def indexing(q):
    while True:
        task = q.get()
        
        documents = task[0]
        collection_name = task[1]
        db_name = task[2]
        operation = task[3]

        if operation=="add":
            dbmap[db_name][collection_name]._add_values_to_unique_indexes(documents)
            dbmap[db_name][collection_name]._add_values_to_text_indexes(documents)
        elif operation=="delete":
            dbmap[db_name][collection_name]._delete_values_from_unique_indexes(documents)
            dbmap[db_name][collection_name]._delete_values_from_text_indexes(documents)

        q.task_done()

  
tinput = threading.Thread(target=indexing, args=(q,))
tinput.daemon = True
tinput.start()  

start_time = time.time()
docs = []
for i in range(100000):
    document = {"name":"Товар -"+str(i),"_id":"id"+str(i)}
    #data =  pickle.dumps(document,pickle.HIGHEST_PROTOCOL)
    docs.append(document)

print("Create set: --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
db['goods_1000000'].insert(docs,upsert=True)
print("Insert many: --- %s seconds ---" % (time.time() - start_time))

"""res = feed(dbmap,[
    {
        "samples_db5": {
            "goods_1": {
                "uid": "23",
                "upsert": {
                    "name": "banana"
                }
            }
        }
    }
])"""

"""res = feed(dbmap,[
    {
        "samples_db5": [
            {
                "goods_1": {
                    "upsert": {
                        
                        "name": "banana"
                    },
                    "uid": "s1"

                }
            },
            {
                "operations_1": {
                    "insert": {
                        
                        "type": "client_operation"
                    },
                    "uid": "s2"
                }
            }
        ]
    }
])


res2 = feed(dbmap,[
    {
        "test_db": {
            "goods_1": {
                "uid": "23",
                "find": {
                    "name": "banana"
                }
            }
        }
    }
])"""

"""

#db['goods2'].register_hash_index("hash_regular","name", dynamic=False) #there are stored indexes
db['goods2'].register_text_index("text_regular","name", dynamic=False) #there are stored indexes

start_time = time.time()
db.initialize()
r = db['goods2'].get_by_index(db["hash_regular"],"товар - 2")
print(r)
#db['goods2'].reindex_hash("hash_regular")
db['goods2'].reindex_text("text_regular")
t = db['text_regular'].search_text_index("Банан")




#db['test_lock'].shrink()

print("Initializing: --- %s seconds ---" % (time.time() - start_time))

id = db["goods2"].insert([{"name":"Банан","_id":"111222"}], upsert=True)
id = db["goods2"].insert([{"name":"Баннер","_id":"11177"}], upsert=True)

id = db["goods2"].insert({"name":"товар - 1"}, upsert=True)

r = db['goods2'].get_by_index(db["hash_regular"],"Банан")
id = db["goods2"].insert([{"name":"Бананан","_id":"111222"}], upsert=True)
r = db['goods2'].get_by_index(db["hash_regular"],"Банан")
r = db['goods2'].get_by_index(db["hash_regular"],"Бананан")

try:
    with DBSession(db) as s:
        
        docs = [{"name":"товар - 1","_id":"12"},{"name":"товар - 2","_id":"121"} ]
        id = db["goods2"].insert(docs, upsert=False, session=s)
        id = db["goods2"].insert(docs, upsert=True, session=s)
except Exception as e:
    print("Транзакция не записана:" + str(e))        
        
#    db["goods2"].delete(id, session=s)
    

#for i in range(10):
#    start_time = time.time()
#    inserted = db['test_lock'].insert({"product_id":11111, "name":"apple","_id":"t_"+str(i)}, upsert=True )
#    print("insert ID: --- %s seconds ---" % (time.time() - start_time))  

#db['test_lock'].delete(["t_2","t_3"])

#res = db['test_lock'].all()


#docs = []
#for i in range(100000):
#    docs.append({"_id":"ttt_"+str(i),"name":"Товар "+str(i)})

#start_time = time.time()
#inserted = db['test_lock'].insert(docs, upsert=True)
#print("Insert many: --- %s seconds ---" % (time.time() - start_time))



#for i in range(100):
    #start_time = time.time()
    #inserted = db['test_lock'].insert({"_id":"t_"+str(i),"product_id":11111, "name":"apple"}, upsert=True )
    #print("upsert ID: --- %s seconds ---" % (time.time() - start_time))      
#    start_time = time.time()
#    doc = db['test_lock'].get("t_"+str(i))
#    print("get ID: --- %s seconds ---" % (time.time() - start_time))

res = db['test_lock'].find({"_id":"t_1"})
start_time = time.time()
doc = db['test_lock'].all()
print("All : --- %s seconds ---" % (time.time() - start_time))    

"""