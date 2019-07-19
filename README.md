# StudentHub
A student-oriented hub for providing and integrating various academic, social, gaming, and other apps


# Installation
// TODO: write a build script for use in ubuntu?

## Install python (if necessary)
First, install python 
`sudo apt-get python3` // TODO: update this command

## Install pip
https://pip.pypa.io/en/stable/installing/

## Install virtualenv
https://virtualenv.pypa.io/en/latest/installation/ <br>
Alternatively you can use virtualenvwrapper for simpler cli commands

## Create virtualenv
`virtualenv -p python3 env/student-hub` <br>
Note: env should not be in version control

## Create project directory and clone repository
// TODO: update this to reflect mk dir and cd
// TODO: add git clone command

## Settings
Settings are read from `~/studenthub/config/settings.json` <br>
Copy contents from `settings_sample.json` to a a new file `settings.json` and modify as 
appropriate. Reach out to fellow contributors as needed for settings.

// TODO: Add more initialization steps

# Model Database Migrations
## Take care committing migrations!
Migrations should made by the developer updating one model at a time. The developer 
should then run `python manage.py makemigrations <app-name>` when committing changes 
to the repository.<br><br>
The following link discusses the issues with conflicts in migrations in vcs.<br>
https://stackoverflow.com/questions/28035119/should-i-be-adding-the-django-migration-files-in-the-gitignore-file