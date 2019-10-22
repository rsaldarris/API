from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.TipoCultivo import TipoCultivo

app = Flask(__name__)
CORS(app)

@app.route('/tipoCultivo', methods=['GET'])
def getAll():
    return (TipoCultivo.list())

@app.route('/tipoCultivo', methods= ['POST'])
def postOne():
    body = request.json
    print("YOLO")
    return (TipoCultivo.create(body))

#app.run(port=5000, debug=True)
