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

def get_executives_from_mongodb():
    client = connect_to_database()
    db = client['AMAND']
    collection = db['executives']
    cursor = collection.find({})
    executives_data = list(cursor)  # Convert cursor to a list of dictionaries
    return executives_data

def get_community_service_from_mongodb():
    client = connect_to_database()
    db = client['AMAND']
    collection = db['community_service']
    cursor = collection.find({})
    community_service_data = list(cursor)  # Convert cursor to a list of dictionaries
    return community_service_data

def get_blog_by_name(name):
    client = connect_to_database()
    db = client['AMAND']
    collection = db['blogs']
    query = {'name': name}
    cursor = collection.find(query)
    blog_data = list(cursor)  # Convert cursor to a list of dictionaries
    if blog_data:
        return blog_data[0]
    else:
        return None

if __name__ == '__main__':

    print(get_community_service_from_mongodb())
