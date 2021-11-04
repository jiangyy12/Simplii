## Phase 2 Improvements
Phase 2 saw many changes in the develpoment of Smiplii. In this document we provide a detailed overview on all the changes implemented by our team during Phase 2.

## Front End
The team worked meticulously to improve the user interface. While revamping the existing UI, we took the liberty to add a couple more features:
The original version did not have a login or signup page. The tasks were displayed in a single page, listed one below the other. The add task section was part of the same page.

*Improvements:*
1) Created a SignUp page to enable new users to create an account to use Simplii.
2) Designed a login page that acts as the portal to sign in once a user has an account.
3) Improved existing UI for viewing all tasks. 
4) Made the user experience more insightful by dividing the tasks based on deadlines into "This week", "Backlog" and "Future Tasks".
5) Created a screen pop-up form for the feature of adding tasks to the pipeline. Also, incorporated an edit button for the same.
6) Color-coded the progress of tasks to make the experience more user friendly. At a glance, the user can now understand the overall progress of his or her tasks. The color scheme that dipicts this:
  -> Red indicates Stuck - This could be the result of a bottleneck in the pipeline or the likes.
  -> Blue indicates In Progress - This shows the tasks that are currently been pursued.
  -> Yellow indicates Waiting - This usually happens when there exists a dependency on someone else to complete the task. For example, if the user wishes the task to be reviewed by someone before marking it as complete.
  -> Green indicates Done - This indicates the task at hand has been completed and is no longer in the pipeline

## Back End
The original version after Phase 1 was not hosted on a backend. Our team strived to host the app on AWS to leverage cloud services and to assist future scalability.

*Improvements:*
1) Redesigned the schema for Simplii - we introduced a new entity called "Categories" into the schema. This feature allows users to tag their tasks under a category of their choice and not limit their choices to "Physical" or "Intellectual" as in the previous version.
2) Hosted the backend on AWS Relational Database Service-RDS
  The AWS Database is used as a primary DB by the location. The application interacts with the DB and no additional steps are required from the users. 
