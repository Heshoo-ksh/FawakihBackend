from app import app
from pymongo import MongoClient, server_api
from instance.config import MONGO_URI

def test_mongo_connection(uri):
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=server_api.ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"An error occurred while trying to ping MongoDB: {e}")

if __name__ == '__main__':
    # Test the MongoDB connection before starting the app
    test_mongo_connection(MONGO_URI)
    app.run(debug=True)
