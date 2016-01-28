from pymongo import MongoClient
from bson.objectid import ObjectId
 
class MongoRepository(object):
    """ Repository implementing CRUD operations on any collection in MongoDB """
 
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.collection = self._get_collection()

    def _get_collection(self):
        return self.repository.mongob[self.collection_name]
 
    def get(self, uuid=None):
        try:
            if uuid is None:
                documents = []
                for document in self.collection.find():
                    del document['_id']
                    documents.append(document)
                return {"status": "ok", self.collection_name: documents}
            else:
                document = self.collection.find_one({"uuid": uuid})
                if document != None:
                    del document["_id"]
                    return {"status": "ok", self.collection_name: document}
                else:
                    return {"status": "error", "reason": "document not found"}
        except Exception as e:
            return {"status": "error", "reason": e}

    def create(self, document):
        try:
            if document is not None:
                document_id = self.collection.insert_one(document).inserted_id
                return {"status": "ok", "uuid": document['uuid']}  
            else:
                return {"status": "error", "reason": "document is None"}
        except Exception as e:
            return {"status": "error", "reason": e}
 
    def update(self, document):
        try:
            if document is not None:
                result = self.collections.find_one_and_update({'uuid': uuid}, 
                                                        {'$set': updated_host})
                return {"status": "ok"}
            else:
                return {"status": "error", "reason": "document is None"}
        except Exception as e:
            return {"status": "error", "reason": e}
 
    def delete(self, document):
        try:
            if document is not None:
                result = self.collections.delete_one({'uuid': uuid})
                return {"status": "ok"}
            else:
                return {"status": "error", "reason": "document is None"}
        except Exception as e:
            return {"status": "error", "reason": e}        