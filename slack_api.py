from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class Slack:

    client = None

    def __init__(self, slack_bot_token):
        self.client = WebClient(token=slack_bot_token)
        
    def sendMessage(self, channel ,text):
        """ Send slack message """

        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=text
            )
            print(response)

        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]  
            print(f"Got an error: {e.response['error']}")


if __name__ == "__main__":  
    slack = Slack("xoxb-")
    slack.sendMessage('cxi_rpa_test', "test")