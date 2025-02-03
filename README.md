
# Student REST API

The **Student REST API** is a Python-based backend application built with **Django** and **Postgres** to perform CRUD operations on student data. This project is designed to be easily deployable both locally and on a Kubernetes cluster.

---

## Technology Stack

- **Backend**: [Python](https://www.python.org/ "Python")  
- **Database**: [Postgres](https://www.postgresql.org/ "Postgres")  
- **Framework**: [Django](https://www.django-rest-framework.org/ "Django")  

---

## Formatters and Linters

- **Flake8**: [Flake8](https://flake8.pycqa.org/en/latest/index.html# "Flake8")  
- **Black**: [Black](https://black.readthedocs.io/en/stable/ "Black")  
- **Isort**: [Isort](https://pycqa.github.io/isort/ "Isort")  

---

## How to Set Up Locally

### Prerequisites

1. Ensure **Postgres** is installed locally. [Installation Guide](https://www.postgresql.org/ "Postgres").  
2. Install **Python** (3.8 or higher).  

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/CyrilBaah/Student-Rest-API.git
   cd Student-Rest-API
   ```

2. **Create a virtual environment** and activate it:
   ```sh
   virtualenv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Rename `env.example` to `.env`.
   - Update the `.env` file with your Postgres credentials and other configurations.

5. **Run migrations**:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**:
   ```sh
   python manage.py runserver
   ```

7. **Access the API**:
   - Open your browser and navigate to: [http://localhost:8000/api/schema/docs#/](http://localhost:8000/api/schema/docs#/ "API Docs").  

---

## API Endpoints

- **POST** `/api/v1/students/` - Add a new student.  
- **GET** `/api/v1/students/` - Get all students.  
- **GET** `/api/v1/students/<id>` - Get a student by ID.  
- **PUT** `/api/v1/students/<id>` - Update a student by ID.  
- **DELETE** `/api/v1/students/<id>` - Delete a student by ID.  
- **GET** `/api/v1/healthcheck/` - Healthcheck endpoint.  

---

## Running the App on Kubernetes

### Prerequisites
- **KinD**: [KinD](https://kind.sigs.k8s.io/ "KinD")  
- **Kubectl** installed and configured.  

### Steps

1. **Apply Kubernetes configurations**:
   ```sh
   kubectl apply -f ops/k8s/app
   ```

2. **Set up secrets**:
   - Rename `secret-example.yml` to `secret.yml`.
   - Update the `secret.yml` file with your environment variables.
   - Apply the secret:
     ```sh
     kubectl apply -f ops/k8s/app/
     ```

3. **Initialize the database**:
   - Get the Postgres pod name:
     ```sh
     kubectl get pods
     ```
   - Access the Postgres pod and create the database:
     ```sh
     kubectl exec -it <db-pod-name> -- psql -U postgres -d postgres
     CREATE DATABASE "db-0";
     exit
     ```

4. **Run migrations**:
   - Get the application pod name:
     ```sh
     kubectl get pods
     ```
   - Access the application pod and run migrations:
     ```sh
     kubectl exec -it <app-pod-name> -- bash
     python manage.py migrate
     exit
     ```

5. **Access the application**:
   - Forward the application port:
     ```sh
     kubectl port-forward <app-pod-name> 8000:8000
     ```
   - Open your browser and navigate to: [http://localhost:8000/api/schema/docs#/](http://localhost:8000/api/schema/docs#/ "API Docs").  

---

## Kubernetes Dashboard Setup

1. **Install the Kubernetes Dashboard**:
   ```sh
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
   ```

2. **Expose the Dashboard**:
   ```sh
   kubectl proxy
   ```

3. **Create a service account**:
   ```sh
   kubectl apply -f ops/k8s/service-account/dashboard-adminuser.yml
   ```

4. **Generate a token**:
   ```sh
   kubectl -n kubernetes-dashboard create token admin-user
   ```
   Copy the generated token.

5. **Access the Dashboard**:
   - Open your browser and navigate to:  
     [http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/ "Kubernetes Dashboard").  
   - Paste the token to log in.

---

## Contributing

Contributions are welcome! Please follow these steps:  
1. Fork the repository.  
2. Create a new branch for your feature or bugfix.  
3. Submit a pull request.  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
