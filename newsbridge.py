import os
from dotenv import load_dotenv

import aiohttp
import discord
from discord.file import File

from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityUrl, MessageEntityTextUrl,\
    MessageEntityBold, MessageEntityItalic, MessageEntityUnderline,\
    MessageEntityStrike, MessageEntityCode


load_dotenv()
# Remember to use your own values from my.telegram.org!
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
tg_client = TelegramClient('anon', API_ID, API_HASH)


# bridge 1
CHAT_ID_1 = int(os.getenv('CHAT_ID_1'))
WEBHOOK_URL_1 = os.getenv('WEBHOOK_URL_1')


@tg_client.on(events.NewMessage(chats=CHAT_ID_1))
async def handler1(event):
    print('got message on chat 1')
    await handler(event.message, WEBHOOK_URL_1)

# bridge 2
CHAT_ID_2 = int(os.getenv('CHAT_ID_2'))
WEBHOOK_URL_2 = os.getenv('WEBHOOK_URL_2')


@tg_client.on(events.NewMessage(chats=CHAT_ID_2))
async def handler2(event):
    print('got message on chat 2')
    await handler(event.message, WEBHOOK_URL_2)

# if you want a third bridge just copy and paste the above code and increment the number


async def handler(m, webhook_url):
    message = improveMessage(m)
    session = aiohttp.ClientSession()
    webhook = discord.Webhook.from_url(webhook_url, session=session)

    if (m.file and not m.web_preview):
        path = await m.download_media()
        print('File saved to', path)  # printed after download is done
        try:
            await webhook.send(file=File(path))
            print('File sent')
        except:
            print('unable to send file')
        os.remove(path)

    if len(message) < 2000:
        print('short message')
        await webhook.send(message)
        print('sent message')
    elif len(message) < 3300:
        print('long message')
        message1 = ''
        message2 = ''
        lines = message.splitlines()
        i = 0
        for x in lines:
            # print(x)
            if i < len(lines)/2:
                message1 = message1 + x + '\n'
            else:
                message2 = message2 + x + '\n'
            i = i+1

        await webhook.send(message1)
        await webhook.send(message2)
        print('sent messages')
    else:
        print('longer message')
        message1 = ''
        message2 = ''
        message3 = ''
        lines = message.splitlines()
        i = 0
        for x in lines:
            # print(x)
            if i < len(lines)*0.3:
                message1 = message1 + x + '\n'
            elif i < len(lines)*0.6:
                message2 = message2 + x + '\n'
            else:
                message3 = message3 + x + '\n'
            i = i+1

        await webhook.send(message1)
        await webhook.send(message2)
        await webhook.send(message3)
        print('sent messages')


def improveMessage(m):
    offset = 0
    try:
        print(m)
        if m.entities:
            for entity in m.entities:
                print(entity)
                if (type(entity) is MessageEntityUrl or type(entity) is MessageEntityTextUrl) and hasattr(entity, 'url'):
                    print('add url')
                    m.message = m.message[:entity.offset+entity.length+offset] + \
                        ' ('+entity.url+') ' + \
                        m.message[offset+entity.offset+entity.length:]
                    offset = offset + len(entity.url) + 4
                elif (type(entity) is MessageEntityUrl):
                    print('other url')
                    if m.message[entity.offset+offset:entity.offset+offset+entity.length].find('http') == -1:
                        m.message = m.message[:entity.offset+offset] + \
                            'https://' + m.message[entity.offset+offset:]
                        offset = offset + 8
                    else:
                        print('had http')
                elif (type(entity) is MessageEntityBold):
                    print('bold')
                    m.message = m.message[:entity.offset+offset] + '**' + m.message[entity.offset+offset:entity.offset +
                                                                                    offset+entity.length-1] + '**' + m.message[entity.offset+offset+entity.length-1:]
                    offset = offset + 4
                elif (type(entity) is MessageEntityItalic):
                    print('italic')
                    m.message = m.message[:entity.offset+offset] + '_' + m.message[entity.offset +
                                                                                   offset:entity.offset+offset+entity.length] + '_' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 2
                elif (type(entity) is MessageEntityUnderline):
                    print('underline')
                    m.message = m.message[:entity.offset+offset] + '__' + m.message[entity.offset +
                                                                                    offset:entity.offset+offset+entity.length] + '__' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 4
                elif (type(entity) is MessageEntityStrike):
                    print('strike')
                    m.message = m.message[:entity.offset+offset] + '~~' + m.message[entity.offset +
                                                                                    offset:entity.offset+offset+entity.length] + '~~' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 4
                elif (type(entity) is MessageEntityCode):
                    print('code')
                    m.message = m.message[:entity.offset+offset] + '`' + m.message[entity.offset +
                                                                                   offset:entity.offset+offset+entity.length] + '`' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 2
        # print(m.message)
        print('improved message')
    except:
        print('weird message')

    # gendersternchen
    m.message = m.message.replace('*', '\*')
    #offset = offset + m.message.count('\*')
    m.message = m.message.replace('\*\*', '**')

    return m.message


print('started')

with tg_client:
    # client.loop.run_until_complete(main())
    tg_client.run_until_disconnected()
