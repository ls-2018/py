from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    pwd = request.form.get("pwd")
    print(username,pwd)
    
    ret_dict = {
        "code":0,
        "msg":"登录成功",
        "data":{
            "user_id":666,
            "username":username,
            "nickname":"xiaowangba"
        }
    }
    
    return jsonify(ret_dict)

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)