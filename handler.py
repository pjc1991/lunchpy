import json
import lunchpy.config as config
import lunchpy.recommend.recommend as recommend
from lunchpy.slack import slack_util


def hello(event, context):
    recommend_msg = recommend.recommend(config.location, config.google_map_key)
    text = slack_util.post_slack_message(recommend_msg['message'], config.channel_id, config.slack_token)
    return text

if __name__ == "__main__":
    hello(None, None)