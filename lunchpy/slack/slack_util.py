from slack_sdk import WebClient

# post slack message to certain channel
# get channel id from config.py
# get slack token from config.py


def post_slack_message(text, channel_id, slack_token):

    # if(config.slack_token == "" or config.channel_id == ""):
    #     # if slack token or channel id is not set, throw error
    #     raise Exception("Slack token or channel id is not set")

    # get slack client
    client = WebClient(token=slack_token)

    # if not joined yet, join the channel
    if not client.conversations_join(channel=channel_id):
        raise Exception("Failed to join channel")

    # print message
    print(f"slackUtil.text: {text}")

    # post message to slack
    client.chat_postMessage(channel=channel_id, text=text)

    return text
