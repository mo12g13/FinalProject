.. Moviesuperfan documentation master file, created by
   sphinx-quickstart on Thu May 11 03:15:29 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Moviesuperfan's documentation!
=========================================
.. toctree::
   :maxdepth: 2

   :caption: Contents:


Introduction
=============
This is a basic web movie application that allows users to keep track of
movies they have watched. This application also provide list of movies that a
a user can watch based on movies that are currently playing in theaters around the
United States.

Requirements:
==============
The following requirements are to be satisfied before you effectively run this project.
The requirements are as follows::
        * requests==2.13.0
        * psycopg2-2.7.1
        * Django==1.11
        * django-crispy-forms==1.6.1
        * Pillow==4.1.1

Installation Instructions
=========================
type the following command:
   >>>  pip install Django==1.11
   >>>  pip install psycopg2-2.7.1
   >>>  pip install requests==2.13.0
   >>>  pip install Pillow==4.1.1

How to run this app
===================
You can run this app by following the below instructions:
On windows command line, type in the following command. We assume that you have
git install on your computer. If you don't have git install, you need to download
git from this url https://git-scm.com/downloads.
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

Run the program
================
      >>> python manage.py migrate
      >>> python manage.py makemigrations
      >>> python manage.py runserver

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
