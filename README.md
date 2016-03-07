=================
Blog Application
=================

Blog application provides a web interface to create stories with title and link.

Overview
--------

Blog application provides a web interfaces to

1. Create a story by giving a title and link. [ Ex - http://localhost:8000/submit/]
2. Up / Down vote individual stories. [Ex - http://localhost:8000/ ]
3. Show top 5 stories (home page). [ Ex - http://localhost:8000/ ]
4. Filter the home page by time (Past 7 hours, 1 day, 7 days) [ Ex- http://localhost:8000/stories/?duration=7 ] , 
   where duration is the number of hours.
5. Comment on stories [ Ex- view comments- http://localhost:8000/story/<story_id>/comments/
			    add comment- http://localhost:8000/story/<story_id>/]
6. Flag stories (admin page, which won’t be shown on the home page. [ http://localhost:8000/admin/ ]

Requirements
------------

* Python 2.7
* If pip in not installed, install it using 
	sudo apt-get install python-pip
* Django 1.7 ( sudo pip install django==1.7 )
* MySQL server ( sudo apt-get install mysql-server )
* mysqldb ( sudo apt-get install python-mysqldb )

Deploying
---------------------------

Database Set up
--------------
1. Create a database in MySQL database. Ex- CREATE DATABASE stories_db;

Update the database configuration in settings.py in the project folder.

DATABASES = 
{
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stories_db',   #database name
        'USER': 'root',		# MySQL user name
        'PASSWORD': 'root12',	# MySQL password
	}
}


2. Run `python manage.py migrate` to create the models. 

Development Server
--------------------

4. Start the development server by running `python manage.py runserver 0.0.0.0:8000`
   and visit http://localhost:8000/submit/ to create a story.

5. Visit http://localhost:8000/ to view the stories and up/down vote them.






