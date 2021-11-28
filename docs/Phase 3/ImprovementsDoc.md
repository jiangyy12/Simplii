## Phase 3 Improvements
Phase 3 saw many changes in the develpoment of Simplii. In this document we provide a detailed overview of all the changes implemented by our team during Phase 3.

## Front End
The team worked meticulously to improve the user interface. While revamping the existing UI, we took the liberty to add a couple more features:
- The original version did not have a page to show the relationship between task and project and all employees. 
- The back to home botton is not that clear in some pages.

*Improvements:*
1) Created a view-task-assignment page to show the relationship between tasks and projects.
2) Created a view-all-employees page to show information of all employees.
3) Created a screen pop-up form for the feature of adding new employee to the system in the view-all-employees page. When adding a new employee, you can also assgin tasks to the new employee.
4) Created a view-all-projects page to show information of all projects.
5) Created a screen pop-up form for the feature of adding new project to the pipeline in the view-all-projects page. 
6) Improved existing UI for viewing all tasks. 
7) In all adding field of a new task or new project, add a new feature "description" for them.


## Back End
Our team strived to host the app on AWS to leverage cloud services and to assist future scalability.

*Improvements:*
1) Redesigned the schema for Simplii - we introduced a new entity called "Project" into the schema. We assumes that one project can have several tasks, and each task can be assigned to several employees, also, one employee can have more than one task. To achieve these assumption, we also create new relationships between Project and tasks, task and employee. Beside, we add new attribute "Desciption" in the task table.

## Comparing Results of Phase 2 and Phase 3


Phase 2                    |  Phase 3
:-------------------------:|:-------------------------:
No view-task-assignment page             |  New view-task-assignment page <img src="https://github.com/jiangyy12/Simplii/blob/main/docs/Phase%203/ScreenShot/%E6%88%AA%E5%B1%8F2021-11-28%20%E4%B8%8B%E5%8D%884.43.12.png" width="500"/>
No view-all-employees page             |  New view-all-employees page <br><img src="https://github.com/jiangyy12/Simplii/blob/main/docs/Phase%203/ScreenShot/%E6%88%AA%E5%B1%8F2021-11-28%20%E4%B8%8B%E5%8D%884.47.32.png" width="500" />
No add-new-employee screen pop-up form             |  New add-new-employee screen pop-up form <br><img src="https://github.com/jiangyy12/Simplii/blob/main/docs/Phase%203/ScreenShot/%E6%88%AA%E5%B1%8F2021-11-28%20%E4%B8%8B%E5%8D%884.50.55.png" width="500" />
All Projects not displayed    |  All Projects displayed <img src="https://github.com/jiangyy12/Simplii/blob/main/docs/Phase%203/ScreenShot/%E6%88%AA%E5%B1%8F2021-11-28%20%E4%B8%8B%E5%8D%884.53.30.png" width="500" />
No page to show the tasks assignment    | new tasks assignment page <img src="https://github.com/jiangyy12/Simplii/blob/main/docs/Phase%203/ScreenShot/%E6%88%AA%E5%B1%8F2021-11-28%20%E4%B8%8B%E5%8D%884.55.49.png" width="500" />
Phase 2 ER <img src="https://github.com/Himanshuu-Gupta/Simplii/blob/main/docs/Phase%202/DB_Schema.jpeg" width="500" height="350" />  | Phase 3 ER <br><img src="https://github.com/jiangyy12/Simplii/blob/main/docs/Phase%203/proj3ER.png" width="500" height="350" />

## Tools used
The original team used Python, HTML, CSS, Bootstrap, JQuery, Javascript, Flask.In addition to these, we have used MySQL, AWS RDS and Python Jinja.
