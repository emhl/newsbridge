# Telegram Channel to Discord Newsbridge

## What does it do?

With this program you can bridge/forward all messages from a Telegram Channel through a Discord Webhook onto your server.

## Installation

- install the latest version of [python](https://www.python.org/)
- clone the project
- install the dependencies with `pip install -r requirements.txt`
- copy the example.env to .env `cp example.env .env`
  
### setting up the telegram side

- either get your Telegram Developer API ID and Hash from [my.telegram.org](https://my.telegram.org/auth) or create a bot with [@BotFather](https://tm.me/BotFather) (the second option only works with public channels or if the bot is in the group/channel and privacy mode is turned off)
- set your API_ID and API_HASH in .env
- get the Telegram Channel ID, you can use this bot [@username_to_id_bot](https://t.me/username_to_id_bot)
- set this value in CHAT_ID_1

### Connecting the Webhook

- create a Discord Webhook [through the server settings](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- copy the Webhook Url and set it to WEBHOOK_URL_1
  
### Final Step

- run it with `python newsbridge.py`
- follow the instructions to authenticate the client.
