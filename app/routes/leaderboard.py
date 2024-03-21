from flask import jsonify
from app import app, mongo  

@app.route('/leaderboard/top', methods=['GET'])
def get_top_documents():
    documents = list(mongo.db.test.find().sort("score", -1).limit(10))
    for document in documents:
        document["_id"] = str(document["_id"])
    return jsonify(documents)

@app.route('/leaderboard/all', methods=['GET'])
def get_all_documents_asc():
    documents = list(mongo.db.test.find().sort("score", -1))
    for document in documents:
        document["_id"] = str(document["_id"])
    return jsonify(documents)
