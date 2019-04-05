from flask import  Flask
from flask_session import Session
from flask import session
from redis import Redis
app = Flask(__name__)
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis("127.0.0.1", 6379, db=7)


Session(app)
@app.route('/')
def index():
    session["user"] == "123"
    # 前端不在储存加密session,而是存储key
    session.get("user")
    return '1'

