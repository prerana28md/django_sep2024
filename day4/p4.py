# Insert a row into the table
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

def insertRow():
    query = 'insert into mobiles(name, price) values(%s, %s)'
    name = input('Enter name of your mobile: ')
    price = float(input('Enter price of your mobile: '))  
    connectionObject = connectDb()
    cursor = connectionObject.cursor()
    cursor.execute(query, (name, price))
    connectionObject.commit()
    cursor.close()
    print('Row is inserted')
    disconnectDb(connectionObject)

insertRow()