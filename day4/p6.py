# Update a row in the table
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

def updateRow():
    query = 'update mobiles set price = %s where id = %s'
    new_price = float(input('Enter new price of mobile: '))
    id = int(input('Enter Id of mobile whose price should be updated: '))  
    connectionObject = connectDb()
    cursor = connectionObject.cursor()
    cursor.execute(query, (new_price, id))
    connectionObject.commit()
    cursor.close()
    print('Row is updated')
    disconnectDb(connectionObject)

updateRow()