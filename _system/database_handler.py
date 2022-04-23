import os
import sqlite3

import mysql
from mysql.connector import connect

from _system import config_manager


class database:
    def __init__(self):
        self.database = os.path.abspath('.') + '/assets/database.db'
        self.prefix = ""

    def sql_switcher(self):
        if self.build_connection_mysql:
            mydb = self.build_connection_mysql
            return mydb
        else:
            return self.build_connection_sqlite()

    def build_connection_mysql(self):
        mysql_data = config_manager.config().mysql_config()
        try:
            connection = mysql.connector.connect(
                host=mysql_data['host'],
                user=mysql_data['user'],
                password=mysql_data['password'],
                database=mysql_data['database']
            )
            return connection
        except:
            return False

    def build_connection_sqlite(self):
        connection = sqlite3.connect(self.database)
        return connection

    def db_insert(self, string):
        connection = self.sql_switcher()
        cursor = connection.cursor()
        cursor.execute(string)
        connection.commit()
        connection.close()

    def db_delete(self, string):
        connection = self.sql_switcher()
        cursor = connection.cursor()
        cursor.execute(string)
        connection.commit()
        connection.close()

    def db_update(self, string):
        connection = self.sql_switcher()
        cursor = connection.cursor()
        cursor.execute(string)
        connection.commit()
        connection.close()

    def db_select(self, string):
        connection = self.sql_switcher()
        cursor = connection.cursor()
        cursor.execute(string)
        fetch = cursor.fetchall()
        connection.close()
        return fetch
