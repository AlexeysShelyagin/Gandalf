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
#   /Schedule - set Gandalf start time, format - "min.sec", example: 17.00
#
#Write bot start command for helper to start this bot
#
#---------------------------------------------------------------#

import requests
import time
import keyboard
import ctypes
import os
import json
from datetime import datetime                                   #not to write "datetime.datetime"

data = json.loads( open('Data.json', 'r').read() )

api_url = data['api_url']
token = data['token']                                           #Bot token url
url = api_url + token + '/'
gandalf_link = data['gandalf_link']                             #Gandalf video link

start_locker = data['start_locker']                             #Start locker
disable_locker = data['disable_locker']                         #Disable locker

update_offset = 0                                               #Offest to avoid updates overflow and recheking old messages
start_minute = -1                                                     #gandalf start minutes 
start_second = -1                                                     #gandalf start seconds

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
    if start_minute == -1:                                      #If not scheluded
        time.sleep(data['after_block_delay'])
    else:                                                       #Waiting for the right time
        while datetime.now().time().minute != start_minute or datetime.now().time().second != start_second:
            time.sleep(0.1)
    os.system('start ' + gandalf_link)                          #Starting the video
    time.sleep(data['before_fullscreen_delay'])
    keyboard.press_and_release('f')                             #F - for fullscreen mode


#---------------------------------------------------------------#


msg = last_update( get_updates_json(url) )                      #Reading old messages to not recheck it later
if msg != '':
    update_offset = msg['update_id']

while True:
    msg = last_update( get_updates_json(url) )                  #Checks anything new from bot

    if msg != '' and msg['update_id'] != update_offset:         #If message is new and it isn't empty

        update_offset = msg['update_id']                        #Not to check one message many times
        master_id = get_chat_id(msg)                            #When scripts start it must run with only one master device

        if msg_text(msg) == '/gandalf':                         #Gandalf
            run_gandalf()
        
        if msg_text(msg) == '/schedule':                        #Set gandalf run time
            while msg['update_id'] == update_offset:            #Waiting message with time
                msg = last_update( get_updates_json(url) )
            start_minute, start_second = map(int, msg_text(msg).split('.'))

        if msg_text(msg) == '/block':                           #Blocking
            os.system(start_locker)

        if msg_text(msg) == '/unblock':                         #Unblocking
            os.system(disable_locker)

        if msg_text(msg) == '/ping':                            #Ping
            send_message(master_id, '.')

        if msg_text(msg) == '/devices':                         #Active devices
            send_message(master_id, str(os.environ['COMPUTERNAME']))
    #time.sleep(100)