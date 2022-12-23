import json
import lunchpy.config as config
import lunchpy.recommend.recommend as recommend
from lunchpy.slack import slack_util
import lunchpy.stores.store_collector as store_collector
import lunchpy_test.test as test


def hello(event, context):
    stores_all = store_collector.get_matzips()
    recommend_matzips = recommend.recommend(stores_all)
    text = slack_util.post_slack_message(recommend_msg(recommend_matzips)["message"])
    return text


def recommend_msg(matzips):
     # make a recommendation message with the selected stores
    message = "오늘 점심은  "
    for matzip in matzips:
        message += f"{matzip.name}"
        if matzip.rating > 0:
            message += f" ({matzip.rating}점)"
        message += ", "

    message = message[:-2] + " 어때요?"

    # Return the recommendation message as the result of the Lambda function
    return {
        "message": message
    }

if __name__ == "__main__":
    hello(None, None)
