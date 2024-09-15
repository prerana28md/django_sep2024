import sys
import pymysql

class DbOperationException(Exception):
    pass

class GameDataOperations:
    def connectDb(self):
        conn = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root@123',
            db='project_db', charset='utf8')
        print('Database connected successfully')
        return conn

    def disConnectDb(self, connection):
        connection.close()
        print('Database disconnected')

    def createTable(self):
        createTableQuery = '''
        CREATE TABLE IF NOT EXISTS games (
            id INT PRIMARY KEY AUTO_INCREMENT, 
            name VARCHAR(50) NOT NULL, 
            price INT, 
            CONSTRAINT new CHECK(price % 100 = 0), 
            mininum_players INT DEFAULT(1), 
            maximum_players INT DEFAULT(11), 
            description TEXT
        );
        '''
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(createTableQuery)
            if returnValue != 0:
                raise DbOperationException
            print('Return value = ', returnValue)
            connection.commit()    
        except DbOperationException:
            print('Error while creating the table Games')
        except pymysql.err.OperationalError:
            print('Operational Error while creating the table Games')
        except Exception as e:
            print('Error in connecting to the database:', e)
        finally:
            cursor.close()
            self.disConnectDb(connection)
            
    def createDb(self):
        createDbQuery = 'CREATE DATABASE IF NOT EXISTS project_db'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            cursor.execute(createDbQuery)
            cursor.close()
        except Exception as e:
            print('Error in connecting to the database:', e)

    def readGameData(self, operation):
        name = input('Enter name of the Game: ')
        price = int(input('Enter Price of the Game (per head): '))
        minPlayers = int(input('Enter minimum number of players: '))
        maxPlayers = int(input('Enter maximum number of players: '))
        if operation == 'insert':
            print('Enter Description of the Game (Max 1000 characters), Use Ctrl+Z to stop: ')
            sys.stdin.flush()
            description = sys.stdin.read().replace('\n', ' ').strip()
            if len(description) > 1000:
                print('Description too long. It should be less than or equal to 1000 characters.')
                return None
            return (name, price, minPlayers, maxPlayers, description)
        id = int(input('Enter Id of the Game to update: '))
        return (name, price, minPlayers, maxPlayers, id)

    def createGame(self):
        insertQuery = 'INSERT INTO games(name, price, mininum_players, maximum_players, description) VALUES(%s, %s, %s, %s, %s)'
        gameObject = self.readGameData('insert')
        if gameObject is None:
            return
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(insertQuery, gameObject)
            print('Return Value = ', returnValue)
            if returnValue != 1:
                raise DbOperationException
            connection.commit()
            print('Row inserted successfully')
        except DbOperationException:
            print('Error while inserting a row')
        except pymysql.err.OperationalError:
            print('Row Insert failed')
        except pymysql.err.ProgrammingError:
            print('Invalid insert command given')
        except Exception as e:
            print('Some Unknown Error occurred:', e)
        finally:
            cursor.close()
            self.disConnectDb(connection)

    def updateGame(self):
        updateQuery = 'UPDATE games SET name = %s, price = %s, mininum_players = %s, maximum_players = %s WHERE id = %s'
        gameObject = self.readGameData('update')
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(updateQuery, gameObject)
            connection.commit()
            if returnValue != 1:
                print(f'Game with id = {gameObject[4]} not found')
            else:
                print('Row update successful')
        except Exception as e:
            print('Row Update failed:', e)
        finally:
            cursor.close()
            self.disConnectDb(connection)

    def deleteGame(self):
        id = int(input('Enter Id of the Game to be deleted: '))
        deleteQuery = 'DELETE FROM games WHERE id = %s'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(deleteQuery, (id,))
            connection.commit()
            if returnValue != 1:
                print(f'Game with id = {id} not found')
            else:
                print('Row delete successful')
        except Exception as e:
            print('Row Delete failed:', e)
        finally:
            cursor.close()
            self.disConnectDb(connection)

    def searchGame(self):
        id = int(input('Enter Id of the Game to be searched: '))
        searchQuery = 'SELECT * FROM games WHERE id = %s'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            numberOfRows = cursor.execute(searchQuery, (id,))
            if numberOfRows == 0:
                print(f'Game with id = {id} not found')
            else:
                row = cursor.fetchone()
                print('Game Details is: \n', str(row))
            cursor.close()
        except pymysql.err.DataError:
            print('Row Search failed')
        finally:
            self.disConnectDb(connection)

    def listGames(self):
        query = 'SELECT * FROM games'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            numberOfRows = cursor.execute(query)
            rows = cursor.fetchall()
            if not rows:
                print('No games found')
            else:
                for row in rows:
                    print('Game Details is: \n', str(row))
            cursor.close()
        except pymysql.err.DataError:
            print('Row Listing failed')
        finally:
            self.disConnectDb(connection)

class Menu:
    def __init__(self, gameOperations):
        self.gameOperations = gameOperations

    def exitProgram(self):
        exit('End of the program')

    def invalidInput(self):
        print('Invalid input entered')

    def getMenu(self):
        menu = {
            1 : self.gameOperations.createGame,
            2 : self.gameOperations.searchGame,
            3 : self.gameOperations.updateGame,
            4 : self.gameOperations.deleteGame,
            5 : self.gameOperations.listGames,
            6 : self.exitProgram
        }
        return menu

    def runMenu(self):
        menu = self.getMenu()
        while True:
            print('\n 1: Create 2: Search 3: Update 4: Delete 5: ListAll 6: Exit \n Your choice: ')
            choice = int(input())
            menu.get(choice, self.invalidInput)()

def startApp():
    operations = GameDataOperations()
    menu = Menu(operations)
    menu.runMenu()

startApp()
