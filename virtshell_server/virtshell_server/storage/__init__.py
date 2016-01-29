"""
Managment Database
"""
from pymongo import MongoClient

from config import MONGODB

CLIENT = MongoClient(MONGODB)
mongodb = CLIENT.virtshell_server_db