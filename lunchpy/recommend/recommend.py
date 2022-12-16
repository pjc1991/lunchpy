import random
import requests

# Replace with your Google Maps API key


def recommend(matzips):
    # if store is None or len(store) == 0 then raise an exception
    if matzips is None or len(matzips) == 0:
        raise Exception("No stores found")
    

    # show all of them
    # for matzip in matzips:
    #     print(matzip.name)
    #     print(matzip.rating)
    #     print(matzip.address)
    #     print("")

    # sort stores by rating
    matzips = sorted(matzips, key=lambda matzip: matzip.rating, reverse=True)

    size = len(matzips)

    # only use the top 20% of stores
    # if size < 5: just use all of them
    if size > 5:
        matzips = matzips[:int(size * 0.2)]
    
    # randomly select 3 stores
    matzips = random.sample(matzips, 3)

    # sort stores by rating
    matzips = sorted(matzips, key=lambda matzip: matzip.rating, reverse=True)

    # make a recommendation message with the selected stores
    message = "오늘 점심은  "
    for matzip in matzips:
        message += f"{matzip.name}"
        if matzip.rating > 0:
            message += f" ({matzip.rating}점)"
        message += ", "
        
    message = message[:-2] + " 어때요?"
    message += f" (총 {size}개 중)"

    # Return the recommendation message as the result of the Lambda function
    return {
        "message": message
    }
