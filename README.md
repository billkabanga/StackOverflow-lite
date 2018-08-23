[![Build Status](https://travis-ci.org/billkabanga/StackOverflow-lite.svg?branch=API-feat)](https://travis-ci.org/billkabanga/StackOverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/billkabanga/StackOverflow-lite/badge.svg?branch=API-feat)](https://coveralls.io/github/billkabanga/StackOverflow-lite?branch=API-feat)


# StackOverflow-lite
This is a  python version of StackOverflow. A platform for questions and answers.It allows users to post questions and answers respectively.Users can also read different questions and their answers.

## Getting started
The following instructions will help you setup and run the application on your machine.

## Prerequisites
You will need the following:
* Internet
* HTML 5
* GIT
* IDE(preferrably Visual Studio Code)
* Postman
## Project Links.
**User Interface:** The user interface pages for this project are hosted on gh-pages. Follow this link (https://billkabanga.github.io/StackOverflow-lite/)
The link to the github feature branch with code for UI templates: (https://github.com/billkabanga/StackOverflow-lite/tree/feature) 

**API endpoints:** The link to the API-feat branch with the code: (https://github.com/billkabanga/StackOverflow-lite/tree/API-feat)

## Project Functionality.
**Interface**
* User can create an account and sign-in.
* User can search for questions.
* User can view recently posted questions.
* User can accept or reject an answer to his/her question.
* User can post a question.
* User can post an answer to a question.
* User can see the most answered questions.

*API endpoints*
* Fetch all questions.
* Post a question.
* Get a specific question.
* Post an answer to a question.

## Getting the application on the local machine.
Clone the remote repository to you local machine using the following command: `git clone https://github.com/billkabanga/StackOverflow-lite.git`

You can now access the project on your local machine by pointing to the local repository using `cd` and `code .` if using Visual Studio code.
Create a virtual environment in the local repository using the following code: `python -3 -m venv env`
Activate the virtual environment: `env/Scripts/Activate.bat`



## Installing dependencies.
To install all the required extensions for project, use the following command: `pip install -r requirements.txt`

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file and test the endpoints in Postman as shown below:

| url/endpoint                        | Verb          | Action                     |      
| ----------------------------------- |:-------------:|  ------------------------- |
| /api/v1/questions                   | GET           | get all questions          | 
| /api/v1/questions/<int:qnId>        | GET           |specific questions          | 
| /api/v1/questions                   | POST          | add questions              |
| /api/v1/questions/<int:qnId>/answers| POST          | add an answer to a question|
  

**Running unittests for the API endpoints**
Use the `pytest qns_api/tests --cov=qns_api/api --cov-report term-missing`  command to run the tests and get the coverage report.

>These tests should be performed in the virtual environment

## Deployment:
Heroku links: (https://bill-stack-over-flow.herokuapp.com/) (https://git.heroku.com/bill-stack-over-flow.git)

## Built with:
**User Interface**
* HTML5
* CSS3

**API endpoints**
* Python 3
* Flask
* Flask-restful

## Author:
Author of this project-Twinomuhwezi Kabanga Bill, 
a young aspiring software developer utilising each day as one to learn and provide solutions to world problems.
