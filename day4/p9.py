# List all Rows of the table
import pymysql

def connectDb():
    connectionObj = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root@123',
            db='prerana_db', charset='utf8')
    print('Database connected successfully')
    return connectionObj

def disconnectDb(conn):
    conn.close()
    print('Database disconnected successfully')

def printMobiles(rows):
    print('ID  NAME         PRICE ')
    print('-' * 22 )
    for row in rows:
        print('%-3s %-12s %s'%(row[0], row[1], row[2]))

def listAllRows():
    query = 'select * from mobiles'
    connectionObject = connectDb()
    cursor = connectionObject.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows == None:
        print(f'No Mobiles were found')
    else:
        printMobiles(rows)
        #for row in rows:
         #   print(f'ID:{row[0]}, Name:{row[1]}, Price:{row[2]}')
    cursor.close()
    disconnectDb(connectionObject)

listAllRows()