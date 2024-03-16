from bson import ObjectId
from flask import jsonify, request
from app import app, mongo  # Import the app and mongo instances

# Create (POST)
@app.route('/test', methods=['POST'])
def create_document():
    data = request.json
    result = mongo.db.test.insert_one(data)
    return jsonify({"success": True, "id": str(result.inserted_id)}), 201

# Read (GET)
@app.route('/test', methods=['GET'])
def get_documents():
    documents = list(mongo.db.test.find())
    for document in documents:
        document["_id"] = str(document["_id"])
    return jsonify(documents)

# Read specific document by ID (GET)
@app.route('/test/<id>', methods=['GET'])
def get_document(id):
    document = mongo.db.test.find_one({"_id": ObjectId(id)})
    if document:
        document["_id"] = str(document["_id"])
        return jsonify(document)
    else:
        return jsonify({"error": "Document not found"}), 404

# Update (PUT)
@app.route('/test/<id>', methods=['PUT'])
def update_document(id):
    data = request.json
    result = mongo.db.test.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count:
        return jsonify({"success": True, "updated": id})
    else:
        return jsonify({"error": "Document not found or no update was necessary"}), 404

# Delete (DELETE)
@app.route('/test/<id>', methods=['DELETE'])
def delete_document(id):
    result = mongo.db.test.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"success": True, "deleted": id})
    else:
        return jsonify({"error": "Document not found"}), 404
