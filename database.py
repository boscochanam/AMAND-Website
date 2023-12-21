import pymongo

connection_string = "mongodb+srv://amandpune:amandpunedatabase@cluster0.2n6kilc.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = client['AMAND']

def get_blogs_from_mongodb():
    collection = db['blogs']
    cursor = collection.find({})
    blog_data = list(cursor)  # Convert cursor to a list of dictionaries
    return blog_data

def get_blog_by_name(name):
    blogs = get_blogs_from_mongodb()
    for blog in blogs:
        if blog['name'] == name:
            return blog
    return None

def get_news_from_mongodb():
    collection = db['news']
    query = {}
    cursor = collection.find(query)
    news_data = list(cursor)
    return news_data

def get_executives_from_mongodb():
    collection = db['executives']
    cursor = collection.find({})
    executives_data = list(cursor)  # Convert cursor to a list of dictionaries
    return executives_data

def get_community_service_from_mongodb():
    collection = db['community_service']
    cursor = collection.find({})
    community_service_data = list(cursor)  # Convert cursor to a list of dictionaries
    return community_service_data

if __name__ == '__main__':
    print(get_community_service_from_mongodb())
