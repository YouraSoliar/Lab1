### LAB3

**1** Setup nessesary packets
pipent install django

**2** Created new Django project and filled all created files on one level above
pipenv run django-admin startproject my_site

**3** Run Django server and opened it on browser
pipenv run python3 manage.py runserver

**4** Stoped server and commited it
Ctrl+C

**5** Created template of main app which will contain all my site`s web pages
pipenv run python3 manage.py startapp main

**6** Created file .html and urls.py
touch templates.html
touch urls.py

**8** Creating pages of two tipes 
first from .html
second from JSON

**9** Filling file urls.py

**10** Run server and committing it

**11** Creating monitoring.py for server monitoring and set up library
pipenv install requests

**12** Opening /health page

**13** Adding error logging if the monitoring will not connect to the server
Adding periodic monitoring by time.sleep() function
Adding alias for faster startup of server
[scripts]
server = "python3 manage.py runserver"

