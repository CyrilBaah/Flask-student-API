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


# Student API  documentation | 
Access the API via [ URL](http://localhost:8000/api/schema/docs#/ "URL") 
- POST /api/v1/students/ - Add a new student.
- GET /api/v1/students/ - Get all students.
- GET /api/v1/students/<id> - Get a student by ID.
- PUT /api/v1/students/<id> - Update a student by ID.
- DELETE /api/v1/students/<id> - Delete a student by ID.
- GET /api/v1/healthcheck/ - Healthcheck endpoint.

# Kubebenetes Dashboard
1. Install
```sh
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```
2. Expose
```sh
kubectl proxy
``
```sh
kubectl -n kubernetes-dashboard create token admin-user
```
3. Authentication
```sh
kubectl apply -f ops/k8s/service-account/dashboard-adminuser.yml
```
4. Generate token
```sh
kubectl -n kubernetes-dashboard create token admin-user
```
Copy the generated token and paste it into the dashboard
5. Access the Dashboard
```sh
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```