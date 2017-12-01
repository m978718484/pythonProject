from flask import Flask, request
from auto.get_data import getData
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
if __name__ == '__main__':
    app.debug = False
    app.run()

