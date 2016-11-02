
from flask import Flask, jsonify
import metacritic

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['DEBUG'] = False
	
@app.route('/')
def index():
    file = open('readme.md','r')
    return file.read()

@app.route('/games',methods=['GET'])
def games():
	return jsonify(metacritic.games())

@app.route('/games/<string:name>',methods=['GET'])
def game_name(name):
	return jsonify(metacritic.games(name))
	
if __name__ == '__main__':
    app.run()