import json
import random
import requests
import sys

import config

# Replace with your Google Maps API key
API_KEY = config.google_map_key


def lambda_handler(event, context):
    # Extract the user's workspace location from the event data
    location = event["location"]

    # Use the Google Maps API to find stores near the user's workspace
    # language should be set to Korean
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=50000&type=restaurant&language=ko&key={API_KEY}"
    response = requests.get(url)

    #if response.status_code is not 200 then raise an exception
    json = response.json()
    # print(json)

    stores = response.json()["results"]

    # use page token to get more results
    while "next_page_token" in response.json():
        next_page_token = response.json()["next_page_token"]
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&radius=1000&type=restaurant&language=ko&key={API_KEY}"
        response = requests.get(url)
        stores += response.json()["results"]
    
    


    # if there are no stores near the user's workspace, return an error message
    if not stores:
        return {
            "message": "No stores found near your workspace."
        }
        
    # filter out stores that don't have a rating
    stores = [store for store in stores if "rating" in store]

    # how many stores are there?
    print(f"Found {len(stores)} stores near your workspace.")

    #print all stores one by one
    # for store in stores:
    #     print(store["name"])
    #     print(store["rating"])
    #     print(store["vicinity"])
    #     print("")

    # sort the stores by their rating in descending order if key in store exists
    stores = sorted(stores, key=lambda store: store["rating"], reverse=True)

    # the list of words which shouldn't be in the store name
    bad_words = ["치킨", "피자", "통닭", "강정", "바베큐", "또래오래", "멕시카나", "파파존스"]

    # filter out stores that have bad words in their name
    stores = [store for store in stores if not any(bad_word in store["name"] for bad_word in bad_words)]

    # show all of them
    for store in stores:
        print(store["name"])
        print(store["rating"])
        print(store["vicinity"])
        print("")


    # randomly select three stores from the top 10
    stores = random.sample(stores, 3)

    # make a recommendation message with the selected stores
    message = "오늘 점심은  "
    for store in stores:
        message += f"{store['name']}({store['rating']}), "
    message = message[:-2] + " 어때요?"

    # console message
    # print(f"message: {message}")

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

    # Test the function 100 times
    # for i in range(10):
    #     print("Recommendation:  ")
    #     print(lambda_handler(event, None))

