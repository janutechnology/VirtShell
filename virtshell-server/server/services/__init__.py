"""
virtshell-server Database
"""
import time
from pymongo import MongoClient

from virtshell_server_config import MONGODB
from virtshell_server_error import WrongFieldType

CLIENT = MongoClient(MONGODB)
mongodb = CLIENT.virtshell_server_db
current_time = lambda: int(round(time.time() * 1000))

def mongo_obj(schema):
    def decorator(func):
        def object_check(obj, *args, **kwargs):
            for key in schema:
                if key in obj:
                    if not isinstance(obj[key], schema[key][0]):
                        unicode_exc = schema[key][0] is str and isinstance(obj[key], unicode)
                        if not unicode_exc:
                            raise WrongFieldType(key, obj[key], schema[key][0])
                elif schema[key][1]:
                    obj[key] = schema[key][0]()

            return func(obj, *args, **kwargs)
        return object_check
    return decorator

copy = lambda x: x.copy() if isinstance(x, dict) else x
def mongo(func):
    def wrapper(*args, **kwargs):
        copy_args = []
        for arg in args:
            copy_args.append(copy(arg))

        return func(*copy_args)
    return wrapper
