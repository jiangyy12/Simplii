import unittest
from sql_helper import sql_helper

class Database_Table_Test(unittest.TestCase):
    #Check number of tables
    def test_number_of_tables(self):
        sqlObj = sql_helper()
        tables = sqlObj.run_query("Show tables")
        numOfTables = len(tables)
        self.assertEqual(numOfTables, 4)

    #check if specific table exists or not
    def test_check_table_exists(self):
        sqlObj = sql_helper()
        tables = sqlObj.run_query("Show tables")
        stringTables = str(tables)
        self.assertEqual("Login_info" in stringTables, True)

    #check if there are no other tables
    def test_check_table_doesnot_exists(self):
        sqlObj = sql_helper()
        tables = sqlObj.run_query("Show tables")
        stringTables = str(tables)
        self.assertNotEqual("Dummy table" in stringTables, True)

    def test_number_of_tables(self):
        sqlObj = sql_helper()
        tables = sqlObj.run_query("Show tables")
        numOfTables = len(tables)
        self.assertNotEqual(numOfTables, 5)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
