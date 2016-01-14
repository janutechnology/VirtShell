import services
import json

@services.mongo
def create_host(**kwargs):
    host_id = services.mongodb.hosts.insert_one(kwargs).inserted_id
    return {"_id": str(host_id)}