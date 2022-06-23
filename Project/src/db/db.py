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

def execute_and_return_all(sql:str,val=None):
    #open connection
    connect = establish()
    cursor = connect.cursor()

    if val == None:
        cursor.execute(sql)
    else:
        cursor.execute(sql,val)
    
    #get values
    values = cursor.fetchall()

    #close connection
    cursor.close()
    connect.close()
    
    return values

def execute_and_return_one(sql:str,val=None):
    #open connection
    connect = establish()
    cursor = connect.cursor()
    if val == None:
        cursor.execute(sql)
    else:
        cursor.execute(sql,val)
    
    #get values
    values = cursor.fetchone()

    #close connection
    cursor.close()
    connect.close()
    
    return values

def connect_execute_close(sql):
    connect = establish()
    cursor = connect.cursor()
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    shut_down(connect)
    return True

def connect_execute_close_with_val(sql,val):
    connect = establish()
    cursor = connect.cursor()
    cursor.execute(sql,val)
    connect.commit()
    cursor.close()
    shut_down(connect)
    return True

# create_food_table_sql = "CREATE TABLE IF NOT EXISTS food
    # (food_id INT NOT NULL, 
    # Name VARCHAR(255), 
    # price DECIMAL(4,2) NOT NULL, 
    # vegan TINYINT NOT NULL, 
    # active TINYINT NOT NULL);"

