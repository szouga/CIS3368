#call the creds, crudoperations, and sql tabs(?)
import mysql.connector
from mysql.connector import Error

#create a connection function
def create_con(hostname, uname, passwd, dbname):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = uname,
            password = passwd,
            database = dbname
        )
        print("Connection is successful")
    except Error as e: #e is like a variable that you can use like x in algebra
        print("connection failed with error: ", e)
    return connection
con = create_con('cis3368classdb.cuu5dov2ewb1.us-east-1.rds.amazonaws.com','admin','Sponge1010?','cis3368dclassdb')
mycursor = con.cursor(dictionary=True)
sql = "select * from user" #select in sql will select the entire table from user
mycursor.execute(sql)
tablerows = mycursor.fetchall() #fetchall will go "fetch" the rows
print(tablerows)

for eachrow in tablerows:
    print(eachrow['lastname']) #maybe try a nested for loop because you have to calculate the prices so you hsve to retrieve eachrow[-1]
    
    