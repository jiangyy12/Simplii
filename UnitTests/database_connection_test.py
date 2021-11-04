import unittest
from sql_helper import sql_helper

class Database_Connection_Test(unittest.TestCase):
    def test_check_AWS_RDS_connection_tables(self):
        sqlObj = sql_helper()
        tables = sqlObj.run_query("Show tables")
        print(tables)
        self.assertEqual(tables != None, True)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
