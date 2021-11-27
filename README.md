# OLX-clone
OLX-clone using python,django,postgresql database and pg-admin 

![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) 
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) 

## Getting Started
### Prerequisites

Make sure you have installed  *python3*, *pip package installer*, *pgadmin4* and *postgresql* before running the project.

### Installation

* Clone the repo
   sh
   git clone {repository link}
   
* Open the migrations in home folder of the project and delete all the migration files which are numbered.
* Install postgresql and Pg-admin in your system.
* Create a database in pg admin.
* Update the database name and password in *settings.py* file of AMS folder to connect the database to our project.
* Change the directory to the place where manage.py file is available.
* Create a virtual environment
   * pip install virtualenvwrapper-win
   * mkvirtualenv 'name of your environment'
   
* Work on the created environment

   * workon 'name of your environment'
   
* Install the following pacakges using command prompt in the virtual environment
   
   * pip install django
   * pip install psycopg2
 
   
* Create django migrations for database using the following commands
   
   * python manage.py makemigrations
   * python manage.py sqlmigrate home 0001
   * python manage.py migrate
   
* Create a super user i.e, the admin
   
   python manage.py createsuperuser
   
   * The command prompt will ask for the username and password for the admin.
   * enter the required details
   
* Run the server and open the website at http://127.0.0.1:8000/ localhost
   
   python manage.py runserver
   






