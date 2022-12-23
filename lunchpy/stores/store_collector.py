# get stores from google
# Compare this snippet from lunchpy/recommend/recommend.py:
import json
import time
import requests
import lunchpy.stores.blacklist as blacklist
from lunchpy.stores.matzip import Matzip
from lunchpy.config import google_map_key, naver_client_id, naver_client_secret, location_name, location

# get stores from google maps api
# will use text search api
def get_matzips_from_google():

    # create query dict
    querydict = {
        "query": f"{location_name} 맛집",
        "language": "ko",
        "location": location,
        "radius": 5000,
        "type": "restaurant",
        "key": google_map_key
    }

    # create query string
    query_string = createQuery(querydict)

    # get stores from google
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?{}".format(
        query_string)

    response = requests.get(url)

    # print response
    # print(response.text)

    # if response.status_code is not 200 then raise an exception
    if response.status_code != 200:
        raise Exception("Failed to get stores from google")

    stores = response.json()["results"]

    print("store count: {}".format(len(stores)))

    # use page token to get more results
    while "next_page_token" in response.json():
        # 2 seconds delay
        time.sleep(2)
        next_page_token = response.json()["next_page_token"]
        print("getting more stores : " + next_page_token)
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={}&key={}".format(
            next_page_token, google_map_key)
        response = requests.get(url)
        print("response : " + response.text)
        stores += response.json()["results"]

    # print all stores with indent
    # print(json.dumps(stores, indent=4, ensure_ascii=False))

    # filter out stores that don't have a rating
    stores = [store for store in stores if "rating" in store]

    # remove stores that have bad words in their name
    bad_words = blacklist.get_bad_words()
    stores = [store for store in stores if not any(
        bad_word in store["name"] for bad_word in bad_words)]

    # turn stores into matzip objects

    matzips = []
    for store in stores:
        # name, store, address
        name = store["name"].strip()
        rating = store["rating"]
        address = store["formatted_address"]
        matzips.append(Matzip(name, rating, address, 0))

    return matzips

# get stores from naver api
def get_matzips_from_naver():

    querydict = {
        "query": f"{location_name} 맛집",
        "display": 100,
        "start": 1,
        "sort": "random",
    }

    query_string = createQuery(querydict)

    # get stores from naver
    url = "https://openapi.naver.com/v1/search/local.json?{}".format(
        query_string)
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    response = requests.get(url, headers=headers)

    # if response.status_code is not 200 then raise an exception
    json = response.json()

    stores = response.json()["items"]

    # remove stores that have bad words in their name
    bad_words = blacklist.get_bad_words()
    stores = [store for store in stores if not any(
        bad_word in store["title"] for bad_word in bad_words)]

    # turn stores into matzip objects
    matzips = []
    print("store count: {}".format(len(stores)))
    print(stores)
    for store in stores:
        name = store["title"].strip()
        rating = 0
        address = store["address"]
        matzips.append(Matzip(name, rating, address, 0))

    return matzips

# get restaurants from google places nearby search api
def get_matzips_from_google_places():
    
        # create query dict
        querydict = {
            "location": location,
            "radius": 5000,
            "type": "restaurant",
            "key": google_map_key
        }
    
        # create query string
        query_string = createQuery(querydict)
    
        # get stores from google
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?{}".format(
            query_string)
    
        response = requests.get(url)
    
        # print response
        # print(response.text)
    
        # if response.status_code is not 200 then raise an exception
        if response.status_code != 200:
            raise Exception("Failed to get stores from google")
    
        stores = response.json()["results"]
    
        print("store count: {}".format(len(stores)))
    
        # use page token to get more results
        while "next_page_token" in response.json():
            # 2 seconds delay
            time.sleep(2)
            next_page_token = response.json()["next_page_token"]
            print("getting more stores : " + next_page_token)
            url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={}&key={}".format(
                next_page_token, google_map_key)
            response = requests.get(url)
            print("response : " + response.text)
            stores += response.json()["results"]
    
        # print all stores with indent
        # print(json.dumps(stores, indent=4, ensure_ascii=False))
    
        # filter out stores that don't have a rating
        stores = [store for store in stores if "rating" in store]
    
        # remove stores that have bad words in their name
        bad_words = blacklist.get_bad_words()
        stores = [store for store in stores if not any(
            bad_word in store["name"] for bad_word in bad_words)]
    
        # turn stores into matzip objects
    
        matzips = []
        for store in stores:
            # name should be trimmed
            name = store["name"].strip()
            rating = store["rating"]
            address = store["vicinity"]
            matzips.append(Matzip(name, rating, address, 0))
    
        return matzips

# get stores from all sources
def get_matzips():
    google_matzips = get_matzips_from_google()
    google_place_matzips = get_matzips_from_google_places()
    naver_matzips = get_matzips_from_naver()
    print(f"google_matzips: {len(google_matzips)}")
    print(f"google_place_matzips: {len(google_place_matzips)}")
    print(f"naver_matzips: {len(naver_matzips)}")
    # combine all matzips
    matzips = google_matzips + naver_matzips + google_place_matzips
    # remove duplicates
    matzips = list(set(matzips))
    return matzips


def createQuery(dict):
    query = ""
    for key in dict:
        query += key + "=" + str(dict[key]) + "&"
    return query[:-1]
