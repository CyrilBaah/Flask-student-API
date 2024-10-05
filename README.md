# Student Rest API
The Student Rest API is to perform operations on student data utilizing a Python backend with Django and Postgres for the database.


## Technology Stack
- [Python](https://www.python.org/ "python")
- [Postgres](https://www.postgresql.org/ "Postgres")
- [Django](https://www.django-rest-framework.org/ "Django")

## Formatter or Linters
- [Flake8](https://flake8.pycqa.org/en/latest/index.html# "Flake8")
- [Black](https://black.readthedocs.io/en/stable/ "Black") 
- [Isort](https://pycqa.github.io/isort/ "Isort")

## How to set up locally 
### Prerequisite
- Make sure **Postgres** is installed locally. *Checkout installation here* [Postgres](https://www.postgresql.org/ "Postgres")

1. Clone the project.
```sh
 git clone https://github.com/CyrilBaah/Student-Rest-API.git
```
```sh
 cd Student-Rest-API
```
2. Create a virtual environment and activate it
```sh
 virtualenv env
 source env/bin/activate  
```
3. Install packages
```sh
 pip install -r requirements.txt 
```
4. Change the env.example file to .env and update it accordingly
5. Run migrations
```sh
python manage.py migrate
```
5. Start server
```sh
python manage.py runserver
```
5. Access the [Student API](http://127.0.0.1:8000/api/schema/docs "Student API")
