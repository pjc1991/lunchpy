import json
import random
import requests

# Replace with your Google Maps API key
API_KEY = "YOUR_API_KEY"


def lambda_handler(event, context):
    # Extract the user's workspace location from the event data
    location = event["location"]

    # Use the Google Maps API to find stores near the user's workspace
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=500&type=store&key={API_KEY}"
    response = requests.get(url)
    stores = response.json()["results"]

    # Choose a random store from the list of stores near the user's workspace
    store = random.choice(stores)

    # Use the store's name and address to construct a recommendation message
    message = f"How about trying {store['name']} for lunch? It's located at {store['formatted_address']}."

    # Return the recommendation message as the result of the Lambda function
    return {
        "message": message
    }
