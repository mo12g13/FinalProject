## Moviesuperfan’s documentation!
Official documentation url http://moviesuperfan.readthedocs.io/en/latest/

Introduction
This is a basic web movie application that allows users to keep track of movies they have watched. This application also provide list of movies that a  user can watch based on movies that are currently playing in theaters around the United States.

Requirements:
The following requirements are to be satisfied before you can effectively run this project. The requirements are as follows:
```
* requests==2.13.0
* psycopg2-2.7.1
* Django==1.11
* django-crispy-forms==1.6.1
* Pillow==4.1.1
```
## Installation Instructions
type the following command:
```
>>>  pip install Django==1.11
>>>  pip install psycopg2-2.7.1
>>>  pip install requests==2.13.0
>>>  pip install Pillow==4.1.1
```
## How to run this app
You can run this app by following the below instructions: On windows command line, type in the following command. We assume that you have git install on your computer. If you don’t have git install, you need to download git from this url https://git-scm.com/downloads.
```
>>> git clone https://github.com/mo12g13/FinalProject
>>> cd C:\Users\Momo Johnson\Documents\FinalProject
***Set your password using the environment variable below for postgres like so
>>> SET POSTGRES_MOVIESUPERFAN_USER_PASSWORD='YourPasswordGoesHere'
*** set your api key so that you can be
able to have access to themoviedb.org
>>> SET API_KEY='Yourapikeygoeshere'
*** After setting your api key, execute the
following script to populate the database with data
>>> python movie_data.py
```
## Run the program
```
>>> python manage.py migrate
>>> python manage.py makemigrations
>>> python manage.py runserver
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
