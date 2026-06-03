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
