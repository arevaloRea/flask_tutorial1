from flask import Flask

app = Flask(__name__)

@app.ruote('/')
def hello():
    return 'Hello, World'
