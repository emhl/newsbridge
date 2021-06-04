import asyncio
import discord
from telethon import TelegramClient, events
from telethon.events.newmessage import NewMessage
from telethon.events import newmessage
from discord import Webhook, RequestsWebhookAdapter
from telethon.tl.types import MessageEntityUrl, MessageEntityTextUrl,\
    MessageEntityBold, MessageEntityItalic, MessageEntityUnderline,\
    MessageEntityStrike, MessageEntityCode, MessageMediaWebPage
from discord.file import File

# Remember to use your own values from my.telegram.org!
api_id = 1234567
api_hash = '1234512345123451234512345'
tg_client = TelegramClient('anon', api_id, api_hash)


#primary
telegram_chat1 = -100000000000
webhook_id_1 = 99999999999999999999
webhook_token_1 ='eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
username1 = 'name1'


#secondary
telegram_chat2 = -100000000000
webhook_id_2 = 99999999999999999999
webhook_token_2 ='eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
username2 = 'name2'


print('started')
    
@tg_client.on(events.NewMessage(chats=telegram_chat1))
async def handler1(event):
    print('got message')
    m= event.message
    message = improveMessage(m)
    
    webhook = Webhook.partial(webhook_id_1, webhook_token_1, adapter=RequestsWebhookAdapter())
    
    if (m.file and not m.web_preview):
        path = await m.download_media()
        print('File saved to', path)  # printed after download is done
        try:
            webhook.send(file=File(path), username=username2)
        except:
            print('unable to send file')
    
    if len(message)<2000:
        print('short message')
        webhook.send(message, username=username1)
        print('sent message')
    elif len(message)<3300:
        print('long message')
        message1 = ''
        message2 = ''
        lines = message.splitlines()
        i = 0
        for x in lines:
            #print(x)
            if i < len(lines)/2:
                message1 = message1 + x + '\n'
            else:
                message2 = message2 + x + '\n'
            i = i+1
        
        webhook.send(message1, username=username1)
        webhook.send(message2, username=username1)
        print('sent messages')
    else:
        print('longer message')
        message1 = ''
        message2 = ''
        message3 = ''
        lines = message.splitlines()
        i = 0
        for x in lines:
            #print(x)
            if i < len(lines)*0.3:
                message1 = message1 + x + '\n'
            elif i < len(lines)*0.6:
                message2 = message2 + x + '\n'
            else:
                message3 = message3 + x + '\n'
            i = i+1
        
        webhook.send(message1, username=username1)
        webhook.send(message2, username=username1)
        webhook.send(message3, username=username1)
        print('sent messages')

@tg_client.on(events.NewMessage(chats=telegram_chat2))
async def handler2(event):
    print('got message')
    m= event.message
    message = improveMessage(m)
    print(message)
    print(len(message))
    
    webhook = Webhook.partial(webhook_id_2, webhook_token_2, adapter=RequestsWebhookAdapter())
    if (m.file and not m.web_preview):
        path = await m.download_media()
        print('File saved to', path)  # printed after download is done
        try:
            webhook.send(file=File(path), username=username2)
        except:
            print('unable to send file')
    
    
    if len(message)<2000:
        print('short message')
        webhook.send(message, username=username2)
        print('sent message')
    elif len(message)<3300:
        print('long message')
        message1 = ''
        message2 = ''
        lines = message.splitlines()
        i = 0
        for x in lines:
            #print(x)
            if i < len(lines)/2:
                message1 = message1 + x + '\n'
            else:
                message2 = message2 + x + '\n'
            i = i+1
        
        webhook.send(message1, username=username2)
        webhook.send(message2, username=username2)
        print('sent messages')
    else:
        print('longer message')
        message1 = ''
        message2 = ''
        message3 = ''
        lines = message.splitlines()
        i = 0
        for x in lines:
            #print(x)
            if i < len(lines)*0.3:
                message1 = message1 + x + '\n'
            elif i < len(lines)*0.6:
                message2 = message2 + x + '\n'
            else:
                message3 = message3 + x + '\n'
            i = i+1
        
        webhook.send(message1, username=username2)
        webhook.send(message2, username=username2)
        webhook.send(message3, username=username2)
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
                    m.message = m.message[:entity.offset+entity.length+offset] + ' ('+entity.url+') ' + m.message[offset+entity.offset+entity.length:]
                    offset = offset + len(entity.url) + 4
                elif (type(entity) is MessageEntityUrl):
                    print('other url')
                    if m.message[entity.offset+offset:entity.offset+offset+entity.length].find('http') == -1:
                        m.message = m.message[:entity.offset+offset]+ 'https://' + m.message[entity.offset+offset:]
                        offset = offset + 8
                    else:
                        print('had http')
                elif (type(entity) is MessageEntityBold ):
                    print('bold')
                    m.message = m.message[:entity.offset+offset] + '**' + m.message[entity.offset+offset:entity.offset+offset+entity.length-1] + '**' + m.message[entity.offset+offset+entity.length-1:]
                    offset = offset + 4
                elif (type(entity) is MessageEntityItalic ):
                    print('italic')
                    m.message = m.message[:entity.offset+offset] + '_' + m.message[entity.offset+offset:entity.offset+offset+entity.length] + '_' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 2
                elif (type(entity) is MessageEntityUnderline ):
                    print('underline')
                    m.message = m.message[:entity.offset+offset] + '__' + m.message[entity.offset+offset:entity.offset+offset+entity.length] + '__' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 4
                elif (type(entity) is MessageEntityStrike ):
                    print('strike')
                    m.message = m.message[:entity.offset+offset] + '~~' + m.message[entity.offset+offset:entity.offset+offset+entity.length] + '~~' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 4
                elif (type(entity) is MessageEntityCode ):
                    print('code')
                    m.message = m.message[:entity.offset+offset] + '`' + m.message[entity.offset+offset:entity.offset+offset+entity.length] + '`' + m.message[entity.offset+offset+entity.length:]
                    offset = offset + 2
        #print(m.message)
        print('improved message')
    except:
        print('weird message')
        
    #gendersternchen
    m.message= m.message.replace('*','\*')
    #offset = offset + m.message.count('\*')
    m.message= m.message.replace('\*\*','**')
    
    return m.message

async def postImage(m):
    if m.photo:
            path = await m.download_media()
            print('File saved to', path)  # printed after download is done

with tg_client:
    #client.loop.run_until_complete(main())
    tg_client.run_until_disconnected()
    
