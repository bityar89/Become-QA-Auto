import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()