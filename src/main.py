from flask import Flask, Response
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello')
@cross_origin()
def hello_world():
    resp = '{"message":"Hello, World!"}'
    return Response(resp, mimetype='application/json')
