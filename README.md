# Simplii
*Make Multitasking Manageable!*
#
**Task Scheduler Web App**

[![DOI](https://zenodo.org/badge/419134447.svg)](https://zenodo.org/badge/latestdoi/419134447)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release](https://img.shields.io/github/release/Himanshuu-Gupta/Simplii)](https://github.com/Himanshuu-Gupta/Simplii/releases/tag/simplii)
![GitHub issues](https://img.shields.io/github/issues-raw/Himanshuu-Gupta/Simplii)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/Himanshuu-Gupta/Simplii)
![Github pull requests](https://img.shields.io/github/issues-pr/Himanshuu-Gupta/Simplii)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://app.travis-ci.com/Himanshuu-Gupta/Simplii.svg?branch=main)](https://app.travis-ci.com/Himanshuu-Gupta/Simplii)
[![CodeCov%](https://codecov.io/gh/Himanshuu-Gupta/Simplii/branch/main/graph/badge.svg?token=GWJMXVPNBY)](https://codecov.io/gh/Himanshuu-Gupta/Simplii)
[![Codecov](https://github.com/Himanshuu-Gupta/Simplii/actions/workflows/codecov.yml/badge.svg)](https://github.com/Himanshuu-Gupta/Simplii/actions/workflows/codecov.yml)

## Why use Simplii?

Planning ahead has never been "Simpl"er! 
<br>
Ever felt that your day went by not as productively as you'd wish? We hear you! With Simplii, you can schedule your tasks and prioritize your efforts based on how you are feeling. Our tool enables the user to efficiently multi-task or switch tasks based on mood to provide a customized user experience while completing routine tasks. `Simplii` parameterizes emotions, deadlines, task difficulty and moods to suggest a task to be done keeping you at your productive best.

## Visual Walkthrough:

https://user-images.githubusercontent.com/18304940/140261087-6491c967-fe11-469f-9718-ca241b690bce.mp4


## Built with:
<table border = "0px">
  <tr>

<code><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-ar21.svg"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_css/w3_css-ar21.svg"></a></code>
<code><a href="https://getbootstrap.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-ar21.svg"></a></code>
<code><a href="https://www.javascript.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/javascript/javascript-ar21.svg"></a></code>
<code><a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg"></a></code>
<code><a href="https://www.mysql.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/mysql/mysql-ar21.svg"></a></code>
<code><a href="https://aws.amazon.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-ar21.svg"></a></code>
    
  </tr>
</table>
<p align="center">
<img src="https://i.giphy.com/media/LMt9638dO8dftAjtco/200.webp" width="150"> <img src="https://i.giphy.com/media/KzJkzjggfGN5Py6nkT/200.webp" width="150"><img src="https://i.giphy.com/media/IdyAQJVN2kVPNUrojM/200.webp" width="150"> <img src="https://media.giphy.com/media/UWt0rhp21JgLwoeFQP/giphy.gif" width ="150"/> <img src="https://media.giphy.com/media/kH6CqYiquZawmU1HI6/giphy.gif" width ="150"/> 
</p>

## Architecture:

ER Diagram                 |  Application Flowchart
:-------------------------:|:-------------------------:
<img src="https://github.com/Himanshuu-Gupta/Simplii/blob/main/docs/Phase%202/DB_Schema.jpeg" width="500" height="350" />  | <img src="https://github.com/ivbhatt/Simplii/blob/main/docs/architectureImages/webappFlowchart.png" width="500" height="350" />

## Quick App Preview:

- **Sign Up Page**
  - User Interface to signup to the app
  <img src="https://user-images.githubusercontent.com/18304940/140264522-ef073322-e3fe-48f6-b785-9688c1225f61.jpeg" width="1000"/>
  
- **Login Page**
  - User Interface to login to the Simplii app. After successful login, user will be redirected to the Dashboard page  
<img src="https://user-images.githubusercontent.com/18304940/140264509-c19cb558-a9b2-462f-94d7-0aea4a9fb601.jpeg" width = "1000"/>

- **View All Tasks** 
  - User interface to view all the tasks the user has created
<img src="https://user-images.githubusercontent.com/18304940/140264503-6019577d-bfae-4592-b935-1d8a497bcc87.jpeg" width="1000" />

- **Add New Tasks** 
  - User interface for adding a new tasks to the portal
<img src="https://user-images.githubusercontent.com/18304940/140264497-c547ed7a-0b67-4f09-b87c-884e3039a462.jpeg" width="1000" />

- **View Current Tasks** 
  - User interface to view current pending tasks
<img src="https://user-images.githubusercontent.com/18304940/140264482-49072881-6613-4e57-a6d2-bfc7960a39bc.jpeg" width="1000"/>

- **View backlog Tasks** 
  - User interface to view all backlog tasks
<img src="https://user-images.githubusercontent.com/18304940/140264488-94925f49-3b8e-48c1-8a8f-1083e26cbe69.jpeg" width="1000"/>


## Getting started:

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/).

   - ### Installation:
      E.g If you downloaded `Python 3.8.7` above, then

      **Steps to setup virtual environment**
     - Create a virtual environment:

        `python3.8 -m venv test_env`
    
     - Activate the virtual environment: 

        `source test_env/bin/activate`
    
     - Build the virtual environment:(must be present in [project directory](./))

        `pip install -r requirements.txt`

  - ### Run Instructions

     **To run/test the site locally:**

     - Clone [Simplii github repo](https://github.com/Himanshuu-Gupta/Simplii/).

     - Navigate to [project directory](./).
  
     - Run `python app.py` or `python3 app.py`

     - Site will be hosted at:
       `http://127.0.0.1:5000/`

## Tools
- Code Formatter: [black](https://github.com/psf/black)
- Syntax and Code Checker: [PyLint](https://pylint.org/)

## Third-Party Tools

- [AWS Relational Database Service-RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
  -  The AWS Database is used as a primary DB by the location. The application interacts with the DB and no additional steps are required from the users. For any contributors or future developers, please mail to himanshu199586@gmail.com to get your AWS IAM user account details to connect to AWS RDS.

## :page_facing_up: License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/Himanshuu-Gupta/Simplii/blob/main/LICENSE) for more details.

## Chat Channel
<code><a href="https://discord.gg/twMMQrUuKB" target="_blank"><img height="100" width="250" src="https://user-images.githubusercontent.com/42767118/135394825-26dee6db-7a64-4e3f-902a-1e35abd4cf0c.png"></a></code>

## Phase 1:

- [x] Create database ER diagram
- [x] Designed application flowchart
- [x] Create Dashboard Page
- [x] Create Add task form
- [x] Setup Flask
- [x] Add Unit testing

## Phase 2:

- [x] Update database ER diagram by including entity "Categories"
- [x] Host application on AWS Relational Database Service
- [x] Create SQL DML and DDL queries
- [x] Improve dashboard UI
- [x] Create Login Page
- [x] Create Signup Page
- [x] Add more unit testing
- [x] Add Error Handling mechanisms
- [x] Create pop-up task adding form
- [x] Color code the varios task based on status
- [x] Prioritize tasks based on deadlines into "This week", "Backlog" and "Future Tasks"
- [x] Established connection between frontend and relational database

### Future Enhancements:

- [ ] CI/CD Build pipeline should be implemented
- [ ] Visualisation on Tasks 
- [ ] User session management needs to be implemented
- [ ] Slack/ Discord Reminders or Subscription
- [ ] Sub-tasks check list within a task


## Contributions to the Project
Please refer to the [Contributing.md](https://github.com/Himanshuu-Gupta/Simplii/blob/main/CONTRIBUTING.md) if you want to contrbute to the Wolftrack source code. Follow all the guidelines mentioned and raise a pull request for the developers to review before the code goes to the main source code.





## Support
For any queries and help, please reach out to us at: aunayak@ncsu.edu

