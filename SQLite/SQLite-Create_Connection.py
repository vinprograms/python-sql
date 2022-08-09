#Vincent Trinh
#8-9-22
#taken from https://realpython.com/python-sql-libraries/
#practice with python and SQL
#this script creates or connects to an SQLite database

import sqlite3
from sqlite3 import Error

def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path) #will create a db if one doesn't already exist at path
            print(f"Connection to SQLite DB at '{path}' was successful.")
        except Error as e:
            print(f"The error '{e}' occured.")

        return connection

connection = create_connection("E:\\GitHub\\python-sql\\SQLite\\sm_app.sqlite")
