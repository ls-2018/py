from flask import Blueprint,request,send_file
from settings import MONGO_DB
from settings import MUSIC_PATH
from settings import IMAGE_PATH
import os

gsanthing = Blueprint("gsanthing",__name__)

@gsanthing.route("/get_audio/<filename>")
def get_audio(filename):
    file_path = os.path.join(MUSIC_PATH,filename)
    return send_file(file_path)

@gsanthing.route("/get_image/<filename>")
def get_image(filename):
    file_path = os.path.join(IMAGE_PATH,filename)
    return send_file(file_path)