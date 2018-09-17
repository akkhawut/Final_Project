from app import app
from flask import jsonify, request

@app.route('/')
@app.route('/index')
def index():

	return jsonify(
        ask= "",
        ans= "",
        distance= ""
    )


@app.route('/post', methods=['POST'])
def postja():
        print( request.get_json() )
	return ""

	
 
