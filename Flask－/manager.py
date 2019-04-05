from flask import Flask
from app01 import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


from werkzeug.serving import run_simple,WSGIRequestHandler
from werkzeug.wrappers import Response,Request
from threading import get_ident
