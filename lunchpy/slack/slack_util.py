from slack_sdk import WebClient
import lunchpy.config as config
def post_slack_message(text):

    # if(config.slack_token == "" or config.channel_id == ""):
    #     # if slack token or channel id is not set, throw error
    #     raise Exception("Slack token or channel id is not set")

    # get slack client
    client = WebClient(token=config.slack_token)

    # if not joined yet, join the channel
    if not client.conversations_join(channel=config.channel_id):
        raise Exception("Failed to join channel")

    # print message
    print(f"slackUtil.text: {text}")

    # post message to slack
    client.chat_postMessage(channel=config.channel_id, text=text)

    return text
