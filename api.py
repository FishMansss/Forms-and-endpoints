from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/question',  methods=['POST'])
def endpiont():
    data = request.form
    print(data)
    output =  f'''
        <!DOCTYPE html>
        <body>
        <h1> hello {data['name1']}! I was hoping you could show me how to...{data['verb']} </h1>
        </body>
        '''    
    return output

app.run(port=5000)
