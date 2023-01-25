from flask import Flask

app = Flask(__name__)

@app.route('/users/hello')
def hello():
    return 'Hello, welcome to the ESBay User API\n'