import mysql.connector
import os

HOST = os.environ.get("DB_HOST")
USERNAME = os.environ.get("DB_USERNAME")
PWD = os.environ.get("DB_PWD")
DBNAME = os.environ.get("DB_NAME")


print(HOST)