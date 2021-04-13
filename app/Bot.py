#bot token: 1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds
#bot link: t.me/screen_gandalf_bot

import requests
import time
import keyboard
import ctypes
import os

api_url = 'https://api.telegram.org/'
token = 'bot1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds'
url = 'https://api.telegram.org/' + token + '/'
gandalf_link = 'https://youtu.be/Sagg08DrO5U'

last_message_id = -1

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

def run_gandalf():
    time.sleep(1)
    keyboard.press_and_release('win+r')
    time.sleep(1)
    keyboard.write('chrome.exe')
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.write(gandalf_link)
    keyboard.press_and_release('enter')
    time.sleep(10)
    keyboard.press_and_release('f')


#---------------------------------------------------------------------------#


msg = last_update( get_updates_json(url) )
last_message_id = msg['message']['message_id']     #not to check messages writed before

while True:
    msg = last_update( get_updates_json(url) )
    if msg != '' and msg['message']['message_id'] != last_message_id:

        last_message_id = msg['message']['message_id']          #not to check one message many times
        master_id = get_chat_id(msg)                        #when scripts start it must run with only one master device

        if msg_text(msg) == '/gandalf':
            print(master_id)
            #os.system('Stand_by.vbs')
            run_gandalf()
        
        if msg_text(msg) == '/ping':
            send_message(master_id, '.')

        if msg_text(msg) == '/devices':
            send_message(master_id, str(os.environ['COMPUTERNAME']))
    #time.sleep(100)