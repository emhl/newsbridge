# Telegram Channel to Discord Newsbridge
## What does it do?
With this program you can bridge/forward all messages from a Telegram Channel through a Discord Webhook onto your server.

## Installation
- download the newsbridge.py
### setting up the telegram side
- get your Telegram Developer API ID and Hash from [my.telegram.org](https://my.telegram.org/auth)
- set your api_id and api_hash in code
- get the Telegram Channel ID, you can use this bot [@username_to_id_bot](https://t.me/username_to_id_bot)
- set your telegram_chat1
### Connecting the Webhook
- create a Discord Webhook [through the server settings](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- copy the Webhook Url and extract the id and token from the url 
- set your webhook_id_1 and webhook_token_1 
- set a username for your webhook in username1
### Final Step
- run it with `python3 newsbridge.py`
- follow the instructions to authenticate the client.
