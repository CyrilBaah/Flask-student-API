 echo -n 'password' | base64 

 echo "cGFzc3dvcmQK"| base64 --decode
 kubectl exec -it <service-name> -- psql -U postgres -d postgres