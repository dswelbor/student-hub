[![Travis build status](https://travis-ci.com/dswelbor/student-hub.svg?branch=master)](https://travis-ci.com/dswelbor/student-hub)

# StudentHub
A student-oriented hub for providing and integrating various academic, social, gaming, and other apps


# Installation
Below are instructions to install necessary services and requirements for this project.
<!--TODO: write a build script for use in ubuntu?-->

## Install PostgreSQL
<!-- TODO: Include instructions for basic PostgreSQL and provide resources for configuration --> 
 PostgreSQL is the recommended Relation Database Management System for storing studenthub data. While other RDMS will 
 likely work, additional configuration/modification might be required 
 1) Install postgresql on your development environment.<br>
 2) Configure postgresql with appropriate settings.
 3) Create username and password for database access.<br>
 4) Create the database django will use ie `studenthub` <br>
 5) Update settings.json to reflect db settings (more on that later)
Alternatively, you can use a remote RDMS (ideally PostgreSQL) if one is available to you. 
Simply update settings.json as appropriate for database access


## Install python (if necessary)
First, install python 
`sudo apt-get python3`

## Install pip
https://pip.pypa.io/en/stable/installing/

## Install virtualenv
https://virtualenv.pypa.io/en/latest/installation/ <br>
Alternatively you can use virtualenvwrapper for simpler cli commands

## Clone repository
From CLI, run the command: <br>`git clone https://github.com/dswelbor/student-hub.git`

## Create virtualenv
From CLI, run the command: <br>
`virtualenv -p python3 env/student-hub` <br>
Note: env should not be in version control, so generally not in same sub directory 
as the local git repo.

## Activate virtualenv
From CLI, run the command: <br>
`source env/student-hub/bin/activate` <br>
This activates the virtual environment. To later deactivate virtualenv, type: `deactivate`

## Install environment requirements
From the virtualenv, navigate to the git repository root folder and run: <br>
`pip install -r requirements.txt`

## Settings
Settings are read from `~/studenthub/config/settings.json` <br>
Copy contents from `settings_sample.json` to a a new file `settings.json` and modify as 
appropriate. Reach out to fellow contributors as needed for settings.

<!-- TODO: Add more initialization steps -->

## Migrations
Apply migrations: `python manage.py migrate` <br>
This applies existing "migrations" from VCS to your database, and defines the schema 
(types/structure/constraints) for the data in the database

## Take care committing migrations!
Migrations should made by the developer updating one model at a time. The developer 
should then run `python manage.py makemigrations <app-name>` when committing changes 
to the repository.<br><br>
The following link discusses the issues with conflicts in migrations in vcs.<br>
https://stackoverflow.com/questions/28035119/should-i-be-adding-the-django-migration-files-in-the-gitignore-file

# Games
## Trivia game
Trivia should be initialized with data using the populate_trivia script. <br>
`python manage.py populate_trivia`
