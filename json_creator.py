import json

# Function to get user input for each field
def get_user_input():
    _id = input("Enter _id (in the format {'$oid': 'your_id'}): ")
    name = input("Enter name: ").replace(" ", "_")  # Replace spaces with underscores in the name
    title = input("Enter title: ")
    content = input("Enter content: ")

    # Input for images, the user can input multiple images
    images = []
    while True:
        image_url = input("Enter image URL (or type 'done' to finish): ")
        if image_url.lower() == 'done':
            break
        image_alt = input("Enter image alt text: ")
        images.append({"url": image_url, "alt": image_alt})

    date = input("Enter date: ")

    # Create a dictionary with the input values
    data = {
        "_id": _id,  # Use _id directly without attempting to load as JSON
        "name": name,
        "title": title,
        "content": content,
        "images": images,
        "date": date
    }

    return data

# Get user input
user_data = get_user_input()

# Output the JSON format
output_json = json.dumps(user_data, indent=2)
print("\nOutput JSON:\n")
print(output_json)
