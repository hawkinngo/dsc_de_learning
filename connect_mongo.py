from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://delearning:spam0123456789@de-learning.wivmj69.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    print("Connected!!!")
    # Create the database for our example (we will use the same database throughout the tutorial
    return client


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    db = get_database()
