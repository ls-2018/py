from flask import Flask, send_file
from app01 import create_app

app = create_app()


@app.route('/static/<filename>')
def get_static(filename):
    return send_file(filename)


if __name__ == '__main__':
    app.run(debug=True)

from werkzeug.serving import run_simple, WSGIRequestHandler
from werkzeug.wrappers import Response, Request
from threading import get_ident
