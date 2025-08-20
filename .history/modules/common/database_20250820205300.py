import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(r"C:\Users\Ярик\Desktop\AutomationGIT\Become-QA-Auto\become_qa_auto.db")
        self.cursor = self.connection.cursor()
        
    def test_connection(self):
        sqlite_select_Query = """SELECT sqlite_version();"""
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print("Connected successfully. SQLite Database version is: ", record) 
        
    def get_all_users(self):
        query = """SELECT name,address, city FROM users"""
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record