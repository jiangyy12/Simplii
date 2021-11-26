import pandas as pd
from src.models.sql_helper import sql_helper

con = sql_helper()

class employee_model:
    def create_employee(self, data):
        columns = ''
        values = ''
        for key, value in data.items():
            columns += str(key) + ', '
            values += "'" + str(value) + "', "

        # query = "INSERT INTO Project (" + columns[:-2] + " ) VALUES (" + values[:-2] + " );"
        query = "INSERT INTO Employee (" + columns[:-2] + " ) VALUES (" + values[:-2] + " );"
        print(query)
        con.run_query(query)
        return

    def get_employee():
        # query = "SELECT ProjectID, ProjectName, Description, Technology FROM Project;"
        query = "SELECT EmployeeID, Name, Age, Skill, Telephone, Title FROM Employee;"
        result = con.run_query(query)
        result = pd.DataFrame(list(result))
        return result.to_dict('records')

    # def update_category(self, data):
    #     values = ''
    #     for key, value in data.items():
    #         values += str(key)+"= '"+str(value)+"', "
    #     query = "UPDATE tasks SET "+values[:-2]+";"
    #     con.run_query(query)
    #     return