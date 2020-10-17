from flask import Flask, Response
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    resp = '{"message":"Hello, World!"}'
    return Response(resp, mimetype='application/json')
