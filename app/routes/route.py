from app import app
from flask import jsonify, request
from app.models.model import YourModel  # Import your model

# Example route
@app.route('/yourRoute', methods=['GET'])
def get_items():
    # Your logic here
    return jsonify({"message": "Success"})
