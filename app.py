  
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    a = 9
    b = 5
    c = a + b
    return 'Hello, World!'
