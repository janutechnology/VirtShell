from storage.mongodb import MongoDB
from config import DATABASE_PROVIDER

class StorageFactory(object):
    @staticmethod
    def get_storage(database_name):
        if DATABASE_PROVIDER == 'mongodb':
            return MongoDB(database_name)