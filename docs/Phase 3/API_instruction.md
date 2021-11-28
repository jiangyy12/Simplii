<h1>API_Instruction</h1>

**Function: /task_controller.py/create_task()**<br>
**Method:POST**<br>
**Description**: Create a new task based on the input from frontend.<br>
**Inputs**: 
- Task Name
- Project
- Category
- Start Date
- Due Date
- Hours
- Description

**Outputs**: None
<br>
<br>



**Function: /task_controller.py/delete_task()**<br>
**Method:DELETE**<br>
**Description**: Delete a task based on the task ID<br>
**Inputs**: 
- Task ID


**Outputs**: None
<br>
<br>


**Function: /task_controller.py/update_task()**<br>
**Method:POST**<br>
**Description**: Update the task information based on the input from frontend.<br>
**Inputs**: 
- Task Name
- Project
- Category
- Start Date
- Due Date
- Hours
- Description


**Outputs**: None
<br>
<br>


**Function: /app.py/view_all_tasks()**<br>
**Method:GET**<br>
**Description**: Get all tasks informations<br>
**Inputs**: None<br>
**Outputs**: 
- Task
- Status
- Category 
- Due Date
- Description
<br>
<br>

**Function: /app.py/view_all_projects()**<br>
**Method:GET**<br>
**Description**: Get all projects informations<br>
**Inputs**: None<br>
**Outputs**: 
- ProjectID
- ProjectName
- Description 
- Technology
<br>
<br>

**Function: /app.py/view_all_employees()**<br>
**Method:GET**<br>
**Description**: Get all employees informations<br>
**Inputs**: None<br>
**Outputs**: 
- EmployeeID
- Name
- Age 
- Skill
- Telephone
- Title
<br>
<br>

**Function: /app.py/create_project()**<br>
**Method:POST**<br>
**Description**: Create a new Project<br>
**Inputs**: 
- EmployeeID
- Name
- Age 
- Skill
- Telephone
- Title


**Outputs**: None

<br>
<br>

**Function: /app.py/create_employee()**<br>
**Method:POST**<br>
**Description**: Create a new Employee<br>
**Inputs**: 
- EmployeeID
- TaskID


**Outputs**: None
<br>
<br>




