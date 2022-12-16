import lunchpy.slack.slack_util as slack_util
import lunchpy.recommend.recommend as recommend
import lunchpy.config as config


if __name__ =='__main__':
    recommend_msg = recommend.recommend(config.location, config.google_map_key)
    slack_util.post_slack_message(recommend_msg['message'], config.channel_id, config.slack_token)
