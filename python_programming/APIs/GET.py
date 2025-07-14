import requests

# use   GET request to fetch data

url = 'https://jsonplaceholder.typicode.com/posts'
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f'status code: {response.status_code}')
        posts = response.json()
        if posts:
            print(f"First Title: {posts[0]['title']}")
        else:
            print("No posts found.")
    else:
        print(f'Failed to retrieve data: {response.status_code}')

if __name__ == "__main__":
    fetch_data(url)
    print("Data fetched successfully.")
else:
    print("This script is intended to be run directly, not imported.")
    print("Exiting the script.")


# use post request to send data
def create_post(title, body, user_id):
    url = 'https://jsonplaceholder.typicode.com/posts'
    post_data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    headers = {
        'Content-Type': 'application/json'}
    response = requests.post(url, json=post_data, headers=headers)
    if response.status_code == 201:
        print(f"Post created successfully: {response.json()}")
    else:
        print(f"Failed to create post: {response.status_code}")

if __name__ == "__main__":
    create_post("Sample Title", "This is a sample body for the post.", 1)
else:       
    print("This script is intended to be run directly, not imported.")
    print("Exiting the script.")