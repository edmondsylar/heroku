from flask import Flask, request, jsonify, make_response
from data import things
app = Flask(__name__)

@app.route('/')
def index():
    return 'this works.........!'

@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/data')
def fetch():
   return ('things {}'.format(things))

if __name__=='__main__':
    app.run(debug=True)
