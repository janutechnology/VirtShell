""" Filename: database
    Description: handle database access
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

import os
import json
import sqlite3
from entities import Request

################################################################################
# Global Variables
################################################################################
database_file = '/var/janu/virtshell_provisioning_agent/vsprovagent.db'

################################################################################
# Database Class
################################################################################
class Database(object):    
    def __init__(self, logger):
        self.logger = logger
        self.database_conn = None

        if not os.path.exists(database_file):
            self.database_conn = sqlite3.connect(database_file,
                                                 timeout=5,
                                                 check_same_thread = False)
            self.logger.info("Database %s doesn't exists..." % database_file)
            cursor = self.database_conn.cursor()
            cursor.execute('''
                CREATE TABLE requests(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    message JSON NOT NULL,
                    status INTEGER DEFAULT 0 NOT NULL, 
                    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    message_log TEXT NULL,
                    status_date TIMESTAMP NULL)
            ''')
            self.database_conn.commit()
            cursor.close()
            self.database_conn.close()
            self.logger.info("Created database successfully...")
        else:
            self.database_conn = sqlite3.connect(database_file)
            self.logger.info("Connected database successfully...")

    def _open_connect(self):
        self.database_conn = sqlite3.connect(database_file,
                                        timeout=5,
                                        check_same_thread = False)

    def _close_connect(self):
        self.database_conn.close()

    def insert_new_request(self, message):
        self._open_connect()
        cursor = self.database_conn.cursor()
        cursor.execute("INSERT INTO requests(message) VALUES(?)", (message,))
        self.database_conn.commit()
        cursor.close()
        self._close_connect()
        self.logger.info("new request inserted %s." % message)
        return cursor.lastrowid

    def update_request(self, request):
        self._open_connect()
        cursor = self.database_conn.cursor()
        cursor.execute("UPDATE requests\
                        SET status = ?,\
                        status_date = date('now'),\
                        message_log = ?\
                        WHERE id = ?", (request['status'],
                                        request['message_log'],
                                        request['id'],))
        self.database_conn.commit()
        cursor.close()
        self._close_connect()

    def get_request(self):
        self._open_connect()
        cursor = self.database_conn.execute("SELECT id, message, date \
                                             FROM requests \
                                             WHERE status = 0 LIMIT 1")
        data = cursor.fetchone()
        if data is not None:
            request = Request(data[0], json.loads(data[1]), 0, data[2])
        else:
            request = None
        self._close_connect()
        return request

