from bson import ObjectId
from flask import jsonify, request
from app import app, mongo  # Import the app and mongo instances
from pymongo.errors import DuplicateKeyError


# Read specific document by ID (GET)
@app.route('/test/<id>', methods=['GET'])
def get_document(id):
    document = mongo.db.test.find_one({"_id": ObjectId(id)})
    if document:
        document["_id"] = str(document["_id"])
        return jsonify(document)
    else:
        return jsonify({"error": "Document not found"}), 404
    
# Create (POST)
# This endpoint should be used to create an instance of the user when appropriate
@app.route('/create', methods=['POST'])
def create_document():
    data = request.json
    try:
        result = mongo.db.test.insert_one(data)
        return jsonify({"success": True, "id": str(result.inserted_id)}), 201
    except DuplicateKeyError:
        return jsonify({"error": "A document with the same username already exists."}), 409

# Update (PUT)
# This Endpoint should be used for the functionalitiy to update the username in the setting page
# This enmdpoint can be used to update the score apon new score record
# How will this be used for both updating the score and username???? 
# Answer: You will need to pass a body param as a json object, when updating the score or username, 
# you can provide a json object with only the param you want ot update, that wiolll look like this: 
#{
#    "score": 67
#}

@app.route('/update/<id>', methods=['PUT'])
def update_document(id):
    print(f"Received update for ID: {id}, Data: {request.json}")  # Debug output
    data = request.json
    try:
        result = mongo.db.test.update_one(
            # id will not need to be wrapped in ObjectID constructer since its already in hex
            {"_id": id}, 
            {"$set": data}
        )

        if result.modified_count:
            return jsonify({"success": True, "updated": id}), 201
        else:
            return jsonify({"error": "Document not found or no update was necessary"}), 200
    except DuplicateKeyError:
        return jsonify({"error":"Update failed due to a duplicate username."}), 409


# Delete (DELETE)
@app.route('/test/<id>', methods=['DELETE'])
def delete_document(id):
    result = mongo.db.test.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"success": True, "deleted": id})
    else:
        return jsonify({"error": "Document not found"}), 404