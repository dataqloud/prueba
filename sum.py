from flask import Flask
app = Flask(__name__)
a = 5
b = 4
c = a + b
@app.route('/')
def hello_world():
    return c
