# harri :)
# SQLite database, includes the reading and writing of SQLite system
# 25.7.23

import sqlite3

class SQLDatabase():
    def __init__(self):
        self.con = sqlite3.connect('cableDatabase.db')
        cur = self.con.cursor()

        # Creates a new table inside of database if not already existing, includes all collumns and appropriate text type for each
        cur.execute("""
        CREATE TABLE IF NOT EXISTS cableDb (
            name TEXT,
            length REAL,
            description TEXT,
            quantity INTEGER,
            location TEXT
        ) """)
    
    # adds new information to the database, information is gained through input by user and added into file system, includes validation of data types
    def addCable(self, data):
        cur = self.con.cursor()
        
        stuff = ['name', 'test again ??????', 'testing 3']
        name = "x"
        special = "f"
        
        # creates a dictionary defining values for each collumn, information from user input and redefined to fit data structure
        # data = {'name': "x", 'description': "y", 'length': 1.2, 'quantity': 4, 'location': "there"}
        
        # f string of information defined from dictionary
        x = f'"{data["name"]}", {data["length"]}, "{data["description"]}", {data["quantity"]}, "{data["location"]}"'
        
        # adds information to database system {} represents items in a dictionary / list previously defined above
        print(f"INSERT INTO cableDb VALUES ({x})")
        cur.execute(f"INSERT INTO cableDb VALUES ({x})")
        
        self.con.commit()
    
    # removes cable from SQLite database, uses information from RowID to identify and remove appropriate cable(s)
    def removeCable(self):
        print('test')

   # gets and fetches all information from the cable database and allows information to be shown in UI
    def getCables(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT * FROM cableDb")
        allCables = res.fetchall()

        print(allCables)

        #print(test)
        #print(self.testing.fetchall())

    # function for sorting cables based off specifications given by User
    def sortCable(self):
        cur = self.con.cursor()
        print('test')

# test = 'testing !!!'

# name2 = input('add name')
# db = SQLDatabase()
# add = input('do you want to add a cable?')

# if add == 'y':
#    db.addCable({'name': f"{name2}", 'description': "yeaaa", 'length': 1.2, 'quantity': 4, 'location': "there"})
#    db.getCables()
# elif add =='no i want to remove pretty please':
#    db.removeCable()
# else:
#    print('ok :(')