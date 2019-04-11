from flask import Blueprint,request,jsonify
from settings import MONGO_DB

content = Blueprint("content",__name__)

@content.route("/content_list",methods=["POST"])
def content_list():
    content = list(MONGO_DB.content.find({}))
    
    for index,item in enumerate(content):
        content[index]["_id"] = str(item.get("_id"))
    
    return jsonify(content)