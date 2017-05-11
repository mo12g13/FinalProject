## Moviesuperfan’s documentation!
Official documentation url http://moviesuperfan.readthedocs.io/en/latest/

Introduction
This is a basic web movie application design for movie lovers. The application allows users to keep track of movies they have watched as well as provide reviews for those movies. Also, this application provides list of movies that are currently playing in theaters within the United States from which a user can decide what movie to go watch. Furthermore, the application provides real time trailer for movies that currently have trailer out. User can a taste of the movie by watching a trailer of a particular movie.

Requirements:
The following requirements are to be satisfied before you effectively run this project. The requirements are as follows:
```
* requests==2.13.0
* psycopg2-2.7.1
* Django==1.11
* django-crispy-forms==1.6.1
* Pillow==4.1.1
* Postgresql
```
## Installation Instructions
type the following command:
```
type the following command:
>>>  pip install Django==1.11
>>>  pip install psycopg2-2.7.1
>>>  pip install requests==2.13.0
>>>  pip install Pillow==4.1.1
Alternatively, you can type
>>> pip install -r requirements.txt #from the root directory
```
## How to run this app
You can run this app by following the below instructions: On windows command line, type in the following commands. We assume that you have git install on your computer. If you don’t have git install, you need to download git from this url https://git-scm.com/downloads.
```
>>> git clone https://github.com/mo12g13/FinalProject
>>> cd C:\Users\<yourusername>\<downloadloaction>\FinalProject
***Set your database password by using the environment variable below like so
>>> SET POSTGRES_MOVIESUPERFAN_USER_PASSWORD='YourPasswordGoesHere'
```
## Run the program
```
>>> python manage.py migrate # Migrate the database
>>> python manage.py makemigrations # Make all migrations
>>> python manage.py createsuperuser # Enter you username and password

*** set your api key so that you can be
able to have access to themoviedb.org
>>> SET API_KEY='Yourapikeygoeshere' # Set your api key
*** After setting your api key, execute the
following script to populate the database with data
>>> python movie_data.py # Populate the database with movies data
>>> python manage.py runserver # Run the local server
```
# Heroku Url
https://moviesuperfans.herokuapp.com

![image](https://cloud.githubusercontent.com/assets/17325437/25932548/8201e370-35d7-11e7-9312-55adddcbcf52.png)

![image](https://cloud.githubusercontent.com/assets/17325437/25932569/a46e6e88-35d7-11e7-91d8-2f5dfa3a54ca.png)

![image](https://cloud.githubusercontent.com/assets/17325437/25932585/c28177d0-35d7-11e7-8c44-2b764605521b.png)

![image](https://cloud.githubusercontent.com/assets/17325437/25946096/415cb5d8-360f-11e7-99e3-c94af2e24720.png)

![image](https://cloud.githubusercontent.com/assets/17325437/25946204/ae1b5238-360f-11e7-9a09-70aff90b334f.png)

[image](https://cloud.githubusercontent.com/assets/17325437/25946204/ae1b5238-360f-11e7-9a09-70aff90b334f.png)
![image](https://cloud.githubusercontent.com/assets/17325437/25946378/6e805d16-3610-11e7-83ef-0db978cee53a.png)
