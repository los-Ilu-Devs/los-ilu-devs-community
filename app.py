from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import bdDao;

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/v0/getAllMembers/', methods=['GET'])
@cross_origin()
def get_all_members():
	all_members = bdDao.get_all_members()
	return jsonify(all_members)

app.run(debug=True, port=5550)