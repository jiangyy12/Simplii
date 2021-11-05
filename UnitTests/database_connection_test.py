import unittest
from sql_helper import sql_helper

class Database_Connection_Test(unittest.TestCase):
    #Check if the connection with AWS is established or not
    def test_check_AWS_RDS_connection_tables(self):
        sqlObj = sql_helper()
        tables = sqlObj.run_query("Show tables")
        print(tables)
        self.assertTrue(tables != None)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
