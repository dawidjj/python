from mysql.connector import connection, Error as DatabaseError

config = {
    'user': 'root',
    'password': 'sssss',
    'host': '127.0.0.1',
    'database': 'python'
}

try:
    connect = connection.MySQLConnection(**config)
    cursor = connect.cursor()
except DatabaseError:
    print('Error' + DatabaseError.errno)
import mysql.connector
# import pymysql.cursors