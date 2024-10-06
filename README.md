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
python manage.py makemigrations
python manage.py migrate
```
6. Start server
```sh
python manage.py runserver
```


# Student API documentation
Access the [Student API](http://127.0.0.1:8000/api/schema/docs "Student API")
- POST /api/v1/students/ - Add a new student.
- GET /api/v1/students/ - Get all students.
- GET /api/v1/students/<id> - Get a student by ID.
- PUT /api/v1/students/<id> - Update a student by ID.
- DELETE /api/v1/students/<id> - Delete a student by ID.
- GET /api/v1/healthcheck/ - Healthcheck endpoint.

Access the [Test Link Checker](http://localhost:8000 "Test Link Checker")
