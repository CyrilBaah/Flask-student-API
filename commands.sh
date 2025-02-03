 echo -n 'password' | base64 

 echo "cGFzc3dvcmQK"| base64 --decode
 kubectl exec -it <pod-name> -- psql -U postgres -d postgres

 CREATE DATABASE "db-0";

 kubectl exec -it student-api-5986dd5fd7-tmdcc -- nc -zv postgres-service 5432

 kubectl exec -it student-api-5986dd5fd7-tmdcc -- bash