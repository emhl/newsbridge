# Telegram Channel to Discord Newsbridge

## What does it do?

With this program you can bridge/forward all messages from a Telegram Channel through a Discord Webhook onto your server.

## Installation

- clone the project
- enter the directory 
- copy the example.env to .env

```bash
git clone https://github.com/emhl/newsbridge.git
cd newsbridge
cp example.env .env
```

### setting up the telegram side

- either get your Telegram Developer API ID and Hash from [my.telegram.org](https://my.telegram.org/auth) or create a bot with [@BotFather](https://tm.me/BotFather) (the second option only works with public channels or if the bot is in the group/channel and privacy mode is turned off)
- set your API_ID and API_HASH in .env
- get the Telegram Channel ID, you can use this bot [@username_to_id_bot](https://t.me/username_to_id_bot)
- set this value in CHAT_ID_1

### Connecting the Webhook

- create a Discord Webhook [through the server settings](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- copy the Webhook Url and set it to WEBHOOK_URL_1

### Final Step

you can either run it with docker or in a python venv (without a virtual environment is strongly discuraged)

#### Python venv

Requirements:
- Python

How to Run
- create venv
- enter the virtual envirenment
- install the dependencies
- run the script
- follow the instructions to authenticate the client.

```bash
python -m venv nb-venv
source nb-venv/bin/activate
pip install -r requirements.txt
python newsbridge.py
```

note: too keep it running you could use something like screen, tmux or docker

#### Docker

Requrements:
- docker
- docker-compose

create a session token `anon.session` by running a temporary container in interacrive mode

```bash
touch anon.session
docker build -t newsbridge .
docker run -it -v ./anon.session:/app/anon.session \
-v ./data:/app/data \
--env-file .env --restart unless-stopped \
newsbridge:latest
```

after that you can run it with docker-compose

```bash
docker-compose up -d
```
