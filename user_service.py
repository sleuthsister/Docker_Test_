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
