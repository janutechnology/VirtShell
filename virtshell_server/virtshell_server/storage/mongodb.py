import storage
from config import MONGODB
from pymongo import MongoClient

class MongoDB(object):
    """ CRUD operations on any collection in MongoDB """
 
    def __init__(self, collection_name):
        CLIENT = MongoClient(MONGODB)
        self.mongodb = CLIENT.virtshell_server_db
        self.collection_name = collection_name
        self.collection = self._get_collection()

    def _get_collection(self):
        return self.mongodb[self.collection_name]
 
    def get(self, key=None, value=None):
        try:
            if key is None and value is None:
                documents = []
                for document in self.collection.find():
                    del document['_id']
                    documents.append(document)
                return {"status": "ok", "documents": documents}
            else:
                document = self.collection.find_one({key: value})
                if document != None:
                    del document["_id"]
                    return {"status": "ok", "document": document}
                else:
                    return {"status": "error", "reason": "document not found"}
        except Exception as e:
            return {"status": "error", "reason": e}

    def create(self, document):
        try:
            if document is not None:
                document_id = self.collection.insert_one(document).inserted_id
                return {"status": "ok"}
            else:
                return {"status": "error", "reason": "document is None"}
        except Exception as e:
            return {"status": "error", "reason": e}
 
    def update(self, key, value, document):
        try:
            if document is not None:
                result = self.collection.find_one_and_update({key: value},
                                                             {'$set': document})
                return {"status": "ok"}
            else:
                return {"status": "error", "reason": "document is None"}
        except Exception as e:
            return {"status": "error", "reason": e}

    def delete(self, key, value):
        try:
            result = self.collection.delete_one({key: value})
            return {"status": "ok"}
        except Exception as e:
            return {"status": "error", "reason": e}

    def get_property(self, property_name, instance, enviroment):
        try:
            data = self.collection.find_one({"instance": instance,
                                             "enviroment": enviroment})
            if data != None:
                if property_name in data:
                    return {"status": "ok", "property": data[property_name]}
                else:
                    return {"status": "error", "reason": "property not found"}
            else:
                return {"status": "error", "reason": "instance or enviroment not found"}
        except Exception as e:
            return {"status": "error", "reason": e}

    def get_all_tasks_by_status(self, status_name):
        try:
            documents = []
            for document in self.collection.find({'status':status_name}):
                del document['_id']
                documents.append(document)
            return {"status": "ok", "tasks": documents}
        except Exception as e:
            return {"status": "error", "reason": e}