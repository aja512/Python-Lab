import mysql.connector
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                             database='login',
                             user='root',
                             password='')

    sql_select_Query = "select * from form"
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    print("Total number of rows in form is - ", cursor.rowcount)
    print ("Printing each row's column values i.e.  form record")
  # for row in records:
  #     print("SId = ", row[0], )
  #     print("SName = ", row[1])
  #     print("AGE  = ", row[2])
  #     print("BRANCH  = ", row[3])
  #     print("EMAIL  = ", row[4])
  #     print("MOB_No  = ", row[5], "\n")

    for row in records:
        print(row[0])
       # print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\n")
    cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")
