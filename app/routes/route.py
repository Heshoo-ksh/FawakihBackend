from app import app, mongo
from flask import Blueprint, jsonify
route = Blueprint('test_mflix_route', __name__)

@app.route('/test_mflix',  methods=['GET'])
def test_mflix():
    # Assuming you want to test the connection by getting one document from the movies collection
    movie = mongo.db.movies.find_one()
    if movie:
        # Convert the _id from ObjectId to string for JSON serialization
        movie['_id'] = str(movie['_id'])
        return jsonify(movie), 200
    else:
        return jsonify({"error": "No movie found"}), 404
