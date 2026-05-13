# Containerized Microservices using Docker

The documentation takes you through the process of creating a simple microservices architecture and then containerizing it using Docker for fast and efficient deployment.


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


#### A. User Service : 

```bash
# A microservice for user service

from flask import Flask, request, jsonify

#requests - the sender
#request - the listener

port=3001
app=Flask(__name__)

#dummy user db
user_db={
    "1":{"user_id":"1","name":"Alice"},
    "2":{"user_id":"2","name":"Bob"}
}


#route the user
@app.route('/users/<user_id>',methods=['GET'])
def get_user(user_id):
    user=user_db.get(user_id)
    if(user):
        return jsonify({"user_id":user_id,"name":user}),200 
    else:
        return jsonify({"Error":"user Not found"}),404

if __name__=="__main__":
    print(f"The User service is running on port : {port}")
    app.run(host="0.0.0.0",port=port)

```


#### B. Task Service : 

```bash
# A microservice for the task service

import requests
from flask import Flask,request,jsonify 

port=3002
app=Flask(__name__)

task_db=[]

# route
@app.route("/tasks",methods=['POST'])
def get_task():
    incoming_data=request.get_json()
    if not incoming_data:
        return jsonify({"Error":"No JSON payload provided"}),400

    user_id=incoming_data.get("userId")
    task_name=incoming_data.get("taskName")

    # Check if the user is valid
    try:
        user_response=requests.get(f"http://user-service:3001/users/{user_id}")
        if(user_response.status_code!=200):
            return jsonify({"Error":"No user found"}),404
        user_data=user_response.json()
        task_details={
            "task_id":len(task_db)+1,
            "user_name":user_data.get("name"),
            "task_name":task_name
        }

        task_db.append(task_details)

        return jsonify({"Message":f"Task created successfully for user {user_id}"}),201
    except requests.exceptions.RequestException:
        return jsonify({"Error":"Failed to connect with the user service"}),500

if __name__=="__main__":
    print(f"Task Service running on port : {port}")
    app.run(host="0.0.0.0",port=port)

```

#### C. Gateway Service : 

```bash
# A gateway service enabling the user and task service to communicate with each other

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS 

# CORS - Cross Origin Resource Sharing

port=3000
app=Flask(__name__)

CORS(app)

#define the user route
@app.route("/users/<user_id>",methods=['GET'])
def get_user(user_id):
    response=requests.get(f"http://user-service:3001/users/{user_id}")
    return jsonify(response.json()),response.status_code 

#define the task route
@app.route("/tasks",methods=['POST'])
def get_task():
    incoming_payload=request.get_json()
    response=requests.post("http://task-service:3002/tasks",json=incoming_payload)
    return jsonify(response.json()),response.status_code 

if __name__=="__main__":
    print(f"Gateway Service running on port : {port}")
    app.run(host="0.0.0.0",port=port)
    
```

#### D. Frontend Service : 

```bash
    <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="'UTF-8">
        <title>My Microservices App</title>
        <style>
            body {font-family:Arial, sans-serif; padding:20px;}
            .box {border:1px solid #ccc; padding: 15px; margin-bottom:20px; max-width:400px;}
            input,button {margin-top:10px; padding:10px;}
        </style>
    </head>
    <body>
        <h1>Microservices Dashboard</h1>
        <div class="box">
            <h3>Find a User</h3>
            <button onclick="fetchUser()">Get User 1</button>
            <pre id="user-output">Waiting for data..</pre>
        </div>
        <div class="box">
            <h3>Create a Task</h3>
            <input type="text" id="userIdInput" placeholder="Enter User ID (e.g. 2)"><br>
            <input type="text" id="taskNameInput" placeholder="Enter Task Name"><br>
            <button onclick="createTask()">Submit Task</button>
            <pre id="task-output">Waiting for data..</pre>
        </div>

        <script>
        const GATEWAY_URL = "http://localhost:3000";

        async function fetchUser() {
            try {
                let response = await fetch(GATEWAY_URL + "/users/1");
                
                // DEFENSIVE CHECK: Did the server return HTML instead of JSON?
                let text = await response.text(); 
                try {
                    let data = JSON.parse(text); // Try to parse as JSON
                    document.getElementById("user-output").innerText = JSON.stringify(data, null, 2);
                } catch (e) {
                    // If it fails, print the raw text/HTML to the screen
                    document.getElementById("user-output").innerText = "CRASH! Server returned: \n" + text;
                }
            } catch (error) {
                document.getElementById("user-output").innerText = "Network Error: Is the Gateway running?";
            }
        }

        async function createTask() {
            let userId = document.getElementById("userIdInput").value;
            let taskName = document.getElementById("taskNameInput").value;

            let payload = {
                "userId": userId,
                "taskName": taskName
            };

            try {
                let response = await fetch(GATEWAY_URL + "/tasks", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });

                // DEFENSIVE CHECK: Did the server return HTML instead of JSON?
                let text = await response.text();
                try {
                    let data = JSON.parse(text); // Try to parse as JSON
                    document.getElementById("task-output").innerText = JSON.stringify(data, null, 2);
                } catch (e) {
                    // If it fails, print the raw text/HTML to the screen
                    document.getElementById("task-output").innerText = "CRASH! Server returned: \n" + text;
                }
            } catch (error) {
                document.getElementById("task-output").innerText = "Network Error: Is the Gateway running?";
            }
        }
    </script>
    </body>
</html>
```


## Deployment using Docker

Deploying our application in a containerized manner leads to : 

    1. Environment consistency
    2. application isolation
    3. Resource utilization efficiency
    4. Fast scaling and efficiency

### Steps : 
#### 1. Create a requirements.txt 
The requirements.txt file acts as the official blueprint for all third-party libraries (like Flask) our application needs to run. Because our Docker base image is a blank slate, this file tells the container exactly which packages to download and install during the build process. This guarantees a consistent, automated, and version-controlled environment across all local machines and production servers.
```bash
requirements.txt

    Flask
    requests
    flask-cors
```


#### 2. Create a Dockerfile 
The Dockerfile holds the environment neede to run our application. It holds the language we used to create the microservice and also all the instructions needed to build the containers. It tells Docker to copy and install all the requirements and then to copy all files and create containers for them. Docker containers communicate with each other via their container names.

```bash
Dockerfile

    #Start with a lightweight LINUX computer that has python pre installed 
    FROM python:3.11-slim

    # Create a folder inside the container called app
    WORKDIR /app

    #Copy the requirements list into the container and install them
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    #Copy all python scripts into the container
    COPY . .
```

#### 3. Create a docker-compose.yml 
A .yml file is used as a coniguration file for our application. It holds the instructions, version and the type (Service, Deployement, Storage) of container created.


```bash
docker-compose.yml

    version: '3.8'
    services:
    # 1. The User Service Container
    user-service:
        build: .
        command: python user_service.py
        ports:
        - "3001:3001"

    # 2. The Task Service Container
    task-service:
        build: .
        command: python task_service.py
        ports:
        - "3002:3002"

    # 3. The API Gateway Container
    gateway:
        build: .
        command: python gateway.py
        ports:
        - "3000:3000"

    # 4. The Frontend Server Container
    frontend:
        image: python:3.11-slim
        working_dir: /app
        volumes:
        - .:/app
        command: python -m http.server 8000
        ports:
        - "8000:8000"
```

#### 4. Run the application

Now that we have our developed application and the Dockerfile, docker-compose.yml, and the requirements.txt saved in our project folder, we can deploy it on docker using docker commands in terminal.




```bash
docker-compose up --build
```
The docker-compose up --build command enables us to run mulitple files at once, unlike manual local hosting where we have to start each microservice on a seperate terminal and start then one by one.

