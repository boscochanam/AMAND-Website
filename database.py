import pymongo

connection_string = "mongodb+srv://amandpune:amandpunedatabase@cluster0.2n6kilc.mongodb.net/?retryWrites=true&w=majority"

def connect_to_database():
    client = pymongo.MongoClient(connection_string)
    return client

def get_events_from_mongodb():
    client = connect_to_database()
    db = client['AMAND']
    collection = db['events']
    cursor = collection.find({})
    event_data = list(cursor)  # Convert cursor to a list of dictionaries
    return event_data

def get_news_from_mongodb():
    client = connect_to_database()
    db = client['AMAND']
    collection = db['news']  
    query = {}  
    cursor = collection.find(query)
    news_data = list(cursor) 
    return news_data

if __name__ == '__main__':

    print(get_news_from_mongodb())
