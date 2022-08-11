#Vincent Trinh
#8-9-22
#taken from https://realpython.com/python-sql-libraries/
#practice with python and SQL
#this script creates or connects to a mySQL database

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_pw, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_pw,
                database=db_name
                )
        print(f"Connection to {db_name} successful")
    except Error as e:
        print(f"The error [{e}] occurred")

    return connection

def create_database(connection, query):
    try:
        cursor = connection.cursor() # the cursor object executes queries
    except Error as e:
        print(f"The error [{e}] occurred")
    try:
        cursor.execute(query) # accepts queries as strings
        print("Database created successfully")
    except Error as e:
        print(f"The error [{e}] occurred")

connection = create_connection("localhost", "root", "LearningSQL2022", "sm_app") # connection object to the database server
#create_database_query = "CREATE DATABASE sm_app"
#create_database(connection, create_database_query)
