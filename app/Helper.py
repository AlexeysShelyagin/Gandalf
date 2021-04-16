#---------------------------------------------------------------#
#
#bot token: 1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds
#bot link: t.me/GandalfScreen_bot
#
#This file can update your bot and do other stuff like autorun
#In telegram you can use:
#   /helper_ping - check if helper is working
#   /helper_start_bot - starts the Gandalf.exe
#   /helper_stop_bot - kills the Gandalf.exe process
#   /helper_update - can update bot configuration:
#        send a file to telegram and it will update/create it in folder with bot (this commdand can't update helper)
#
#---------------------------------------------------------------#

import requests
import os
import json

data = json.loads( open('Data.json', 'r').read() )

api_url = data["api_url"]
token = data["token"]                                           #Bot token url
url = api_url + token + '/'

disable_locker = data["disable_locker"]                         #Locker disabler
disable_bot = data["disable_bot"]                               #Gandalf disabler
start_bot = data["start_bot"]                                   #Gandal starter using silent mode

update_offset = 0                                               #Offest to avoid updates overflow and recheking old messages

def get_response(request):                                      #Gets all from the link
    response = requests.get(request)
    return response.json()

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


#---------------------------------------------------------------#


msg = last_update( get_updates_json(url) )                      #Reading old messages to not recheking it later
update_offset = msg['update_id']

while True:
    msg = last_update( get_updates_json(url) )                  #Checks anything new from bot

    if msg != '' and msg['update_id'] != update_offset:         #If message is new and it isn't empty
        update_offset = msg['update_id']                        #Not to check one message many times
        master_id = get_chat_id(msg)                            #When scripts start it must run with only one master device
        
        if msg_text(msg) == '/helper_ping':                     #Ping 
            send_message(master_id, '.')

        if msg_text(msg) == '/helper_start_bot':                #Starting a bot
            os.system(start_bot)
            send_message(master_id, 'Bot started on ' + str(os.environ['COMPUTERNAME']))
        
        if msg_text(msg) == '/helper_stop_bot':                 #Stoping a bot
            os.system(disable_bot)
            send_message(master_id, 'Bot stoped on ' + str(os.environ['COMPUTERNAME']))
        
        #--------------Updater---------------#

        if msg_text(msg) == '/helper_update':
            os.system(disable_bot)
            os.system(disable_locker)
            
            send_message(master_id, str(os.environ['COMPUTERNAME']) + ' ready for update')
            while msg['update_id'] == update_offset:
                msg = last_update( get_updates_json(url) )                                                  #waiting a file

            file_id = msg['message']['document']['file_id']
            file_name = msg['message']['document']['file_name']                                             #Gets file name
            msg = get_response(api_url + token + '/getFile?file_id=' + file_id)                             #Gets path by id
            file_path = msg['result']['file_path']
            update_file = requests.get(api_url + 'file/' + token + '/' + file_path, allow_redirects=True)   #Reading a file

            open(file_name, 'wb').write(update_file.content)                                                #Writing it