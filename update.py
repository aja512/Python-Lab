import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   conn = mysql.connector.connect(host='localhost',
                             database='login',
                             user='root',
                             password='')
   cursor = conn.cursor()

   print ("Before updating record ")
   sql_select_query = """select * from users where username = '317shweta5014'"""
   cursor.execute(sql_select_query)
   record = cursor.fetchone()
   print (record)

   #Update single record now
   sql_update_query = """Update users set password = 'shweta' where username = '317shweta5014'"""
   cursor.execute(sql_update_query)
   #connection.commit()
   print ("Record Updated successfully ")

   print("After updating record ")
   cursor.execute(sql_select_query)
   record = cursor.fetchone()
   print(record)

except mysql.connector.Error as error :
    print("Failed to update record to database: {}".format(error))
    connection.rollback()

finally:
    #closing database connection.
    if(conn.is_connected()):
        conn.close()
        print("connection is closed")
