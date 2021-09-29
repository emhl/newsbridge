# Telegram Channel to Discord Newsbridge
## What does it do?
With this program you can bridge/forward all messages from a Telegram Channel through a Discord Webhook onto your server.

## Installation
- install the latest version of [python](https://www.python.org/)
- clone the project
- install discord.py and telethon with `pip install -r requirements.txt`
### setting up the telegram side
- either get your Telegram Developer API ID and Hash from [my.telegram.org](https://my.telegram.org/auth) or create a bot with [@BotFather](https://tm.me/BotFather) (the second option only works with public channels or if the bot is in the group/channel and privacy mode is turned off) 
- set your api_id and api_hash in code
- get the Telegram Channel ID, you can use this bot [@username_to_id_bot](https://t.me/username_to_id_bot)
- set your telegram_chat1
### Connecting the Webhook
- create a Discord Webhook [through the server settings](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- copy the Webhook Url and extract the id and token from the url 
- set your webhook_id_1 and webhook_token_1 
- set a username for your webhook in username1
### Final Step
- run it with `python newsbridge.py`
- follow the instructions to authenticate the client.
