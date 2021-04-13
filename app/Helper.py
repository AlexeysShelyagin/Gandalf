#this file can update your bot and do other stuff like autorun

import requests
import os

api_url = 'https://api.telegram.org/'
token = 'bot1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds'
url = 'https://api.telegram.org/' + token + '/'
gandalf_link = 'https://youtu.be/Sagg08DrO5U'

last_message_id = -1

def get_response(request):
    response = requests.get(request)
    return response.json()

def get_updates_json(request):                              #Get all updates from bot
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):                                      #Get only last update from bot
    results = data['result']
    if len(results) == 0:
        return ''
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):                                    #Get chat id from message
    chat_id = update['message']['chat']['id']
    return chat_id

def send_message(chat, text):                               #Send messages
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def msg_text(msg):
    if 'text' in msg['message']:
        return msg['message']['text']
    return ''



msg = last_update( get_updates_json(url) )
last_message_id = msg['message']['message_id']     #not to check messages writed before

while True:
    msg = last_update( get_updates_json(url) )
    if msg != '' and msg['message']['message_id'] != last_message_id:
        last_message_id = msg['message']['message_id']          #not to check one message many times
        master_id = get_chat_id(msg)                        #when scripts start it must run with only one master device

        #--------------Updater---------------#

        if msg_text(msg) == '/helper_update':
            send_message(master_id, 'send a file')
            last_message_id = msg['message']['message_id']
            while msg['message']['message_id'] == last_message_id:
                msg = last_update( get_updates_json(url) )
            #print(msg)

            file_id = msg['message']['document']['file_id']
            file_name = msg['message']['document']['file_name']
            msg = get_response(api_url + token + '/getFile?file_id=' + file_id)
            #print(msg)
            file_path = msg['result']['file_path']
            update_file = requests.get(api_url + 'file/' + token + '/' + file_path, allow_redirects=True)
            open(file_name, 'wb').write(update_file.content)