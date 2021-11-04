## Phase 2 Improvements
Phase 2 saw many changes in the develpoment of Simplii. In this document we provide a detailed overview of all the changes implemented by our team during Phase 2.

## Front End
The team worked meticulously to improve the user interface. While revamping the existing UI, we took the liberty to add a couple more features:
- The original version did not have a login or signup page. 
- The tasks were displayed in a single page, listed one below the other. 
- The add task section was part of the same page.

*Improvements:*
1) Created a SignUp page to enable new users to create an account to use Simplii.
2) Designed a login page that acts as the portal to sign in once a user has an account.
3) Improved existing UI for viewing all tasks. 
4) Made the user experience more insightful by dividing the tasks based on deadlines into "This week", "Backlog" and "Future Tasks".
5) Created a screen pop-up form for the feature of adding tasks to the pipeline. 
6) Incorporated an edit button for editing tasks.
7) Created a Search bar to find tasks easily.
8) Color-coded the progress of tasks to make the experience more user friendly. At a glance, the user can now understand the overall progress of his or her tasks. The color scheme that dipicts this:
    - Red indicates Stuck - This could be the result of a bottleneck in the pipeline or the likes.
    - Blue indicates In Progress - This shows the tasks that are currently been pursued.
    - Yellow indicates Waiting - This usually happens when a task has not been picked up yet or in the case of an existing dependency to complete the task. For example, if the user wishes the task to be reviewed by someone before marking it as complete.
    - Green indicates Done - This indicates the task at hand has been completed and is no longer in the pipeline

## Back End
The original version after Phase 1 was not hosted on a backend. Our team strived to host the app on AWS to leverage cloud services and to assist future scalability.

*Improvements:*
1) Redesigned the schema for Simplii - we introduced a new entity called "Categories" into the schema. This feature allows users to tag their tasks under a category of their choice and not limit their choices to "Physical" or "Intellectual" as in the previous version.
2) Hosted the backend on** AWS Relational Database Service - RDS**. The AWS Database is used as a primary DB by the location. The application interacts with the DB and no additional steps are required from the users. Using AWS will help us scale the project by being capable of processing upto 25000 requests every second.

## Comparing Results of Phase 1 and Phase 2


Phase 1                    |  Phase 2
:-------------------------:|:-------------------------:
No Signup page             |  New Signup page <img src="https://user-images.githubusercontent.com/18304940/140264522-ef073322-e3fe-48f6-b785-9688c1225f61.jpeg" width="500"/>
No Login page              |  New Login page <br><img src="https://user-images.githubusercontent.com/18304940/140264509-c19cb558-a9b2-462f-94d7-0aea4a9fb601.jpeg" width="500" />
<img src="https://github.com/ivbhatt/Simplii/blob/main/docs/Screenshot_Header.PNG" width="250" /><img src="https://github.com/ivbhatt/Simplii/blob/main/docs/Task%20list%20Screenshot.PNG" width="250" /> | <img src="https://user-images.githubusercontent.com/18304940/140264482-49072881-6613-4e57-a6d2-bfc7960a39bc.jpeg" width="500" />
All tasks not displayed    |  All tasks displayed included completed ones <img src="https://user-images.githubusercontent.com/18304940/140264503-6019577d-bfae-4592-b935-1d8a497bcc87.jpeg" width="500" />
Simple task adding functionality in main page.    | Pop-up form to add tasks to pipeline. <img src="https://user-images.githubusercontent.com/18304940/140264497-c547ed7a-0b67-4f09-b87c-884e3039a462.jpeg" width="500"  />
No deadline based buckets  |  Deadline based categories - "This week", "Backlog" and "Future Tasks"<img src="https://user-images.githubusercontent.com/18304940/140264488-94925f49-3b8e-48c1-8a8f-1083e26cbe69.jpeg" width="500" />
Phase 1 ER <img src="https://github.com/ivbhatt/Simplii/blob/main/docs/architectureImages/SE_ERDiagram.png" width="500" height="350" />  | Phase 2 ER <br><img src="https://github.com/Himanshuu-Gupta/Simplii/blob/main/docs/Phase%202/DB_Schema.jpeg" width="500" height="350" />

## Tools used
The original team used Python, HTML, CSS, Bootstrap, JQuery, Javascript, Flask.In addition to these, we have used MySQL, AWS RDS and Python Jinja.

## Conclusion of Phase 2
Working on Phase 2 was an eye-opening simulation of how Software Engineering project development occurs in the real world. Countless brainstorming sessions to whip up a myriad of creative ideas which we brought to fruition, in short, the Phase 2 sojourn was a memorable learning experience. We would like to thank Dr. Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project. We are grateful for the opportunity to work with our friends and colleagues at NCSU - shout out to the original developers Ishaan, Arpitha, Krishika, Unnati and Apurva for their amazing project in Phase 1!
