import unittest
import sqlite3

class TestTravelDB(unittest.TestCase):
    def setUp(self):
        try:
            self.connection = sqlite3.connect("travel.db")
        except sqlite3.Error as e:
            self.fail(f"Failed to connect to database: {e}")
    
    def tearDown(self):
        if self.connection:
            self.connection.close()

    def test_connection_established(self):
        self.assertIsNotNone(self.connection)
        self.assertIsInstance(self.connection, sqlite3.Connection)
    
    def test_guide_table_access(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM GUIDE;")
        rows = cursor.fetchall()
        self.assertGreaterEqual(len(rows), 1, "GUIDE table should contain at least one record")
    
    def test_customer_table_access(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM CUSTOMER;")
        rows = cursor.fetchall()
        self.assertGreaterEqual(len(rows), 1, "CUSTOMER table should contain at least one record")
    
    def test_trip_table_access(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM TRIP;")
        rows = cursor.fetchall()
        self.assertGreaterEqual(len(rows), 1, "TRIP table should contain at least one record")

if __name__ == '__main__':
    unittest.main()
