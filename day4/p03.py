import pymysql

def connectDb(connectionObj):
    try:
        connectionObj = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root@123',
            db='my_database', charset='utf8')
        print('Database connected successfully')
    except:
        print('Error in connecting to the DB')
    return connectionObj

def disconnectDb(conn):
    try:
        conn.close()
    except:
        print('Disconnection failed')
    print('Database disconnected successfully')

connectionObject = None
connectionObject = connectDb(connectionObject)
disconnectDb(connectionObject)