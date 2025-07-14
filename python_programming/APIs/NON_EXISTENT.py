import requests

# handle a non-existent endpoint
def fetch_non_existent_post():
    url = 'https://jsonplaceholder.typicode.com/non_existent_endpoint'
    response = requests.get(url)
    if response.status_code == 404:
        print(f"Error: {response.status_code} - The requested resource was not found.")
    else:
        print(f"Unexpected status code: {response.status_code}")


if __name__ == "__main__":
    fetch_non_existent_post()
    print("Attempted to fetch a non-existent post.")
else:
    print("This script is intended to be run directly, not imported.")
    print("Exiting the script.")
