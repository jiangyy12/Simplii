import pandas as pd
from src.models.sql_helper import sql_helper
from datetime import datetime, timedelta

con = sql_helper()

class task_model:
    def __init__(self):
        pass

    def get_this_week_tasks(self, current_date):
        dt = datetime.strptime(current_date, '%d/%b/%Y')
        start_date = dt - timedelta(days=dt.weekday())
        end_date = start_date + timedelta(days=6)
        query = "SELECT * FROM tasks WHERE (Startdate <="+str(end_date)+" Duedate >="+str(start_date)+') or ' \
                                                                                                  'status ="Incomplete"'
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def get_backlog(self, current_date):
        dt = datetime.strptime(current_date, '%d/%b/%Y')
        start_date = dt - timedelta(days=dt.weekday())
        query = "SELECT  * FROM tasks WHERE Duedate <="+str(start_date)+' and status ="Incomplete"'
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def get_future_tasks(self, current_date):
        dt = datetime.strptime(current_date, '%d/%b/%Y')
        start_date = dt - timedelta(days=dt.weekday())
        end_date = start_date + timedelta(days=6)
        query = "SELECT  * FROM tasks WHERE Startdate >="+str(end_date)
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    def create_tasks(self, data):
        columns = ''
        values = ''
        for key, value in data.items():
            columns += str(key)+', '
            values += "'"+str(value)+"', "

        query = "INSERT INTO tasks ("+columns[:-2]+" ) VALUES (" + values[:-2]+" );"
        con.run_query(query)
        return

    def delete_task(self, taskid):
        query = "DELETE FROM tasks WHERE Taskid ="+ taskid
        con.run_query(query)

    def get_task_by_id(self, taskid):
        query = "SELECT * FROM tasks WHERE Taskid =" + taskid
        result = con.run_query(query)
        return result.to_dict('records')

    def update_task(self, data):
        values = ''
        for key, value in data.items():
            values += str(key)+"= '"+str(value)+"', "
        query = "UPDATE tasks SET "+values[:-2]+";"
        con.run_query(query)
        return

