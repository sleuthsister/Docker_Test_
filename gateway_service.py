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
    
