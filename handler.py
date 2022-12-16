import json
import lunchpy.config as config
import lunchpy.recommend.recommend as recommend
from lunchpy.slack import slack_util
import lunchpy.stores.store_collector as store_collector


def hello(event, context):
    stores = store_collector.get_matzips()
    recommend_msg = recommend.recommend(stores)
    text = slack_util.post_slack_message(
        recommend_msg['message'], config.channel_id, config.slack_token)
    return text


if __name__ == "__main__":
    hello(None, None)
