from sqlite3 import connect
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")

def establish():
    my_connection = pymysql.connect(
        host=my_host,
        user=my_user,
        password=my_password,
        database=my_database
    )
    return my_connection

def shut_down(my_con):
    my_con.close()

def committing(my_con):
    my_con.commit()

def execute(my_con,sql: str,val):
    cursor = my_con.cursor()
    cursor.execute(sql,val)

def the_biz(sql,val):
    connect = establish()
    cursor = connect.cursor()
    cursor.execute(sql,val)
    connect.commit()
    cursor.close()
    shut_down(connect)
    return True
