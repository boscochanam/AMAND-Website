import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="amand"
)



def get_blogs_from_sql():
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT blogs.id, blogs.name, blogs.title, blogs.content, blogs.date,
        GROUP_CONCAT(blog_images.url) AS image_urls
        FROM blogs
        JOIN blog_images ON blogs.id = blog_images.blog_id
        GROUP BY blogs.id, blogs.name, blogs.title, blogs.content, blogs.date;
    """
    cursor.execute(query)
    blog_data = cursor.fetchall()
    cursor.close()
    return blog_data

def get_news_from_sql():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM news"
    cursor.execute(query)
    news_data = cursor.fetchall()
    cursor.close()
    return news_data

def get_executives_from_sql():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM executives"
    cursor.execute(query)
    executive_data = cursor.fetchall()
    cursor.close()
    return executive_data

def get_community_service_from_sql():
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT community_service.id, community_service.title, community_service.description,
        GROUP_CONCAT(community_service_images.image_url) AS image_urls
        FROM community_service
        JOIN community_service_images ON community_service.id = community_service_images.community_service_id
        GROUP BY community_service.id, community_service.title, community_service.description;
    """
    cursor.execute(query)
    community_service_data = cursor.fetchall()
    cursor.close()
    return community_service_data

def get_blog_by_name(name):
    blogs = get_blogs_from_sql()
    for blog in blogs:
        if blog['name'] == name:
            return blog
    return None

if __name__ == '__main__':
    # print(get_blogs_from_sql())
    # print(get_news_from_sql())
    print(get_executives_from_sql())
    executives = get_executives_from_sql()
    for executive in executives:
        print(executive['url'])
    # print(get_community_service_from_sql())
    # print(get_blog_by_name("example"))
    pass
