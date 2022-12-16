import lunchpy.slack.slack_util as slack_util
import lunchpy.recommend.recommend as recommend
import lunchpy.config.config as config


if __name__ =='__main__':
    recommend_msg = recommend.recommend(config.location)
    slack_util.post_slack_message(recommend_msg['message'])
