import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(r'/c/Users/Ярик/Desktop/AutomationGIT/Become-QA-Auto' + r'')
        self.cursor = self.connection.cursor()