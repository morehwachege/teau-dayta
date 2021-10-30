# teau-dayta
Data Science and Analytics Software for Machine Learning and Data Science Department TEAU

## How to install
Cone the repository. Open a commandline in the directory of the project. Download virtualenvironment on the commandline using

``pip install virtualenv``

Create a virtualenvironment

``virtualenv dataenv``

Enter into the environment

``source dataenv/Scripts/activate`` for Windows and

``source dataenv/bin/activate`` for Linux/Mac OS


Install the project requirements using
``pip install -r requirements.txt`` .
To run the project on a webserver at localhost, type

``python manage.py runserver``

or specify a port

``python manage.py runserver 127.0.0.1:8000``
