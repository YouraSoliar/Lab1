**LAB 4**

1. Learned about Docker
2. Checked if docker is installed 
sudo docker -v
sudo docker -h
Execution "sudo docker run docker/whalesay cowsay Docker is fun" in "my_work.log" file
3. Read documentation about Dockerfile
4. Created new Dockerfile with Django from third lab
5. Created new repository in DockerHub
6. Built and Pushed images into the repository
sudo docker build -t yourasoliar/lab_4 .
sudo docker push yourasoliar/lab_4 
7. Run the docker image 
sudo docker run -it --name=django-page --rm -p 8000:8000 yourasoliar/lab_4
Web page works good
8. 
9. 
