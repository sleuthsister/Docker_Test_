# Containerized Microservices using Docker

The documentation takes you through the process of creating a simple microservices architecture and then containerizing it using Docker for fast and efficient deployment.

This project is a containerized microservice architecture built with Python and Flask. It demonstrates a decoupled backend system where independent services handle specific domains (Users and Tasks), communicating with each other internally, and exposing endpoints to a vanilla HTML/JavaScript frontend via an API Gateway.

## Tech Stack

**Development:** Python, JavaScript, HTML

**Deployment:** Docker Desktop



## Development

 ### 1. Create microservices:
We Create 3 microservices :

    1. A User service  - To store user details and verificatiom of user.
    2. A Task service - To Create tasks for existing users.
    3. A Gateway service - To enable user and task services to communicate with each other.
    4. Frontend service - A simple webpage to demonstrate the working of microservices.

Libraries Needed : 

    1. Python Flask library - for Flask, jsonify and request functions
    2. Python requests library - for listening and responding to incoming payload.
    3. Python flask_cors library - for Cross Origin Resource Sharing


## Deployment using Docker

The entire backend ecosystem is containerized using Docker, ensuring perfect parity across local, testing, and production environments.
1. Base Image: python:3.11-slim (Chosen for a lightweight, optimized footprint).
2. Registry: The application image is built and pushed to Docker Hub.
3. Orchestration: Docker Compose is used to define the multi-container environment, manage port mapping, and wire the internal container network.

Deploying our application in a containerized manner leads to : 

    1. Environment consistency
    2. application isolation
    3. Resource utilization efficiency
    4. Fast scaling and efficiency

### Steps : 
#### 1. Create a requirements.txt 
The requirements.txt file acts as the official blueprint for all third-party libraries (like Flask) our application needs to run. Because our Docker base image is a blank slate, this file tells the container exactly which packages to download and install during the build process. This guarantees a consistent, automated, and version-controlled environment across all local machines and production servers.

#### 2. Create a Dockerfile 
The Dockerfile holds the environment neede to run our application. It holds the language we used to create the microservice and also all the instructions needed to build the containers. It tells Docker to copy and install all the requirements and then to copy all files and create containers for them. Docker containers communicate with each other via their container names.
#### 3. Create a docker-compose.yml 
A .yml file is used as a coniguration file for our application. It holds the instructions, version and the type (Service, Deployement, Storage) of container created.

#### 4. Run the application

Now that we have our developed application and the Dockerfile, docker-compose.yml, and the requirements.txt saved in our project folder, we can deploy it on docker using docker commands in terminal.

Project Folder Structure : 

<img width="540" height="194" alt="Screenshot 2026-05-13 151344" src="https://github.com/user-attachments/assets/5ce90604-b83d-473f-be25-08f6ed4db6c2" />


Now, navigate to the project folder in CMD and type in the docker commands : 
```bash
docker-compose up --build
```

<img width="419" height="112" alt="image" src="https://github.com/user-attachments/assets/3bd24210-00b6-4167-b097-bd28eb356ae0" />


The docker-compose up --build command enables us to run mulitple files at once, unlike manual local hosting where we have to start each microservice on a seperate terminal and start then one by one.
The microservices are containerized and the image is created in the docker dashboard! 

<img width="572" height="395" alt="image" src="https://github.com/user-attachments/assets/3d3ee11b-62be-4f57-9965-129d2e6b4db7" />

The containers are up and running!

Docker Dashboard View : Running containers

<img width="952" height="332" alt="image" src="https://github.com/user-attachments/assets/e6518a39-0d09-4c47-9029-e5bb86a48428" />

We then go to the go to the server where out application is deployed (Here, we deployed it on python test server 8000)
The Application is now hosted

<img width="352" height="416" alt="image" src="https://github.com/user-attachments/assets/1647e2f3-460a-403a-b1ca-54e28ed20f9f" />

We can interact with the application and all interactions and status codes are logged in the terminal on Docker Dashboard: 

<img width="308" height="416" alt="image" src="https://github.com/user-attachments/assets/47d8234f-e3b0-41d2-a7d0-1d1feb8d31ae" />

Docker Dashboard View of logs : 
A. User Service : 

<img width="773" height="323" alt="image" src="https://github.com/user-attachments/assets/5e27d0e8-4378-4a02-9cd0-99e1a1bdac93" />

B. Task Service : 

<img width="754" height="304" alt="image" src="https://github.com/user-attachments/assets/44795cf6-2b36-43dc-8ad5-2c33117b6e27" />

C. Gateway Service : 

<img width="767" height="338" alt="image" src="https://github.com/user-attachments/assets/fb381e2b-0f22-4b5b-ab2a-c89bfd0259bb" />


To stop the containers, we can CTRL + C in CMD, or stop then manually from Docker Dashboard. 

<img width="533" height="136" alt="image" src="https://github.com/user-attachments/assets/5b941049-3f38-4854-ab73-8290f11964ed" />

We can create images of our containerized application and upload it on docker hub for other users to pull it and try our application without the hassle of dependency or installing issues!
