from flask import Flask,redirect, url_for, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    return 'Hello, World!'
if __name__ == "__main__":    
   app.run(debug=True)
