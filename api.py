from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def endpiont():
    data = request.form
    print(data)
    output =  print(f"<h1> {data['noun 1']} </h1>")    
    return(output)

app.run(port=5000)

