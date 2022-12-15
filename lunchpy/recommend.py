import json
import random
import requests
import sys

sys.path.append('../lunchpy')
import config

# Replace with your Google Maps API key
API_KEY = config.google_map_key


def lambda_handler(event, context):
    # Extract the user's workspace location from the event data
    location = event["location"]

    # Use the Google Maps API to find stores near the user's workspace
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=5000&type=restaurant&key={API_KEY}"
    response = requests.get(url)

    #if response.status_code is not 200 then raise an exception
    json = response.json()
    # print(json)

    stores = response.json()["results"]

    # if there are no stores near the user's workspace, return an error message
    if not stores:
        return {
            "message": "No stores found near your workspace."
        }

    # Choose a random store from the list of stores near the user's workspace
    store = random.choice(stores)

    # Use the store's name and address to construct a recommendation message
    print(store)
    message = f"How about trying {store['name']} for lunch?"

    # Return the recommendation message as the result of the Lambda function
    return {
        "message": message
    }


if __name__ == "__main__":
    # Test the function locally
    event = {
        "location": "37.5002,127.1006"
    }
    print("Recommendation:  ")
    print(lambda_handler(event, None))
