import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='login',
                             user='root',
                             password='')

   sql_insert_query = """ INSERT INTO `concession`(`ticket_no`, `train_class`, `end_station`, `start_station`, `end_date`, `voucher_no`,`cend_station`, `period`, `ctrain_class`,`username`) VALUES (2345,'first','Vidyavihar','Badlapur','2018-02-02','3533sd','Vidyavihar','Quaterly','first','317priya5014')"""

   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully into concession table")

except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))

finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed") 