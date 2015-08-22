#!/usr/bin/python

""" Filename: database
    Description: Agent for handle containers and virtual machines in a host
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

__version__ = '0.1'

import os
import sqlite3
import simplejson

################################################################################
# Global Variables
################################################################################
database_file = '/var/janu/virtshell_agent/vsagent.db'

################################################################################
# Database Class
################################################################################
class Database(object):    
    def __init__(self, logger):
        self.logger = logger
        self.database_conn = None

        if not os.path.exists(database_file):
            self.database_conn = sqlite3.connect(database_file)
            self.logger.info("Database %s doesn't exists..." % database_file)
            cursor = self.database_conn.cursor()
            cursor.execute('''
                CREATE TABLE requests(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    message JSON NOT NULL,
                    status INTEGER DEFAULT 0 NOT NULL, 
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)
            ''')
            self.database_conn.commit()
            cursor.close()
            self.logger.info("Created database successfully...")
        else:
            self.database_conn = sqlite3.connect(database_file)
            self.logger.info("Connected database successfully...")

    def insert_new_request(self, json_message):
        self.logger.info("new request: %s", json_message)
        str_message = simplejson.dumps(json_message)
        cursor = self.database_conn.cursor()
        cursor.execute("INSERT INTO requests(message) VALUES(?)", (str_message,))
        self.database_conn.commit()
        cursor.close()
