# YourAnimeList
YourAnimeList is a web-site for publishing anime and manga-themed content.
___
## Installation
To install this project you need to clone it from this github repo
```
git clone https://github.com/bitwopi/MyFirstSite.git
```
After you need to create virtual environment in project directory.

 __For windows:__

```
python -m venv venv
venv\Scripts\activate
```
__For Linux:__
```
python -m venv venv
source venv/bin/activate
```

When venv already created you need to install a project dependencies.
```
pip install -r requirements.txt
```

___
## .env
To start up project you need to connect project with database. 
To do this you need to create .env file in project folder and assign values to variables.
```
#DB connection
DB_NAME="your_db_name"
USER="your_username"
PASSWORD="your_db_password"
HOST="yourhost" #usually localhost
SECRET_KEY="your django secret key"
#amount of posts on list pages
POST_NUMBER_IN_PAGE=20
#This variables is necessary for password reset work correctly
EMAIL_HOST_USER="your_email_to_send_reset_letters@gmail.com"
EMAIL_HOST_PASSWORD="your_email_access_token"
```

## Migrations
When it's done you want to make migrations and migrate.
```
cd mysite
python manage.py makemigrations
python manage.py migrate
```
## Run
To run application you need to runserver. You should be in "mysite" directory!
```
python manage.py runserver
```



