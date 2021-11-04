import unittest
from sql_helper import sql_helper
import time
class Database_Table_Test(unittest.TestCase):
    def test_read_operation(self):
        sqlObj = sql_helper()
        task1_details = sqlObj.run_query("select * from Tasks where TaskID = 1")
        task1_details = str(task1_details)
        self.assertTrue('Complete SE homework' in task1_details)

    def test_update_operation(self):
        sqlObj = sql_helper()
        task1_update = sqlObj.run_query("Update Tasks set Taskname = 'Apply for google summer internship' where TaskID = 2")
        task1_details = sqlObj.run_query("select * from Tasks where TaskID = 2")
        task1_details = str(task1_details)
        self.assertTrue('Apply for google summer internship' in task1_details)

    def test_insert_operation(self):
        sqlObj = sql_helper()
        addTask= sqlObj.run_query('Insert into Tasks Values ( 1000,1, "Get milk and bread", 1, "Waiting", "2021-11-02", "2021-11-06", 4)')
        task_details = sqlObj.run_query('select * from Tasks where Taskname = "Get milk and bread"')
        task_details = str(task_details)
        self.assertTrue('Get milk and bread' in task_details)
        

    def test_delete_operation(self):
        sqlObj = sql_helper()
        deleteTask= sqlObj.run_query('Delete from Tasks where TaskID=1000')
        task_details = sqlObj.run_query('select * from Tasks where Taskname = "Get milk and bread"')
        task_details = str(task_details)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
