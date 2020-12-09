#bot token: 1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds
#bot link: t.me/screen_gandalf_bot

import requests
import time
import requests
import keyboard
import ctypes

url = "https://api.telegram.org/bot1462769482:AAEU84lWytoJNXkt5bf6rVGjX_fqpqV71ds/"
gandalf_link = "https://youtu.be/Sagg08DrO5U"

last_message_id = -1

def get_updates_json(request):                              #Get all updates from bot
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):                                      #Get only last update from bot
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):                                    #Get chat id from message
    chat_id = update['message']['chat']['id']
    return chat_id

def send_message(chat, text):                               #Send messages
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

while True:
    msg = last_update( get_updates_json(url) )

    if msg['message']['message_id'] != last_message_id:
        last_message_id = msg['message']['message_id']          #not to check one message many times
        master_id = get_chat_id(msg)                        #when scripts start it must run with only one master device

        #----------------------------GANDALF-----------------------------------
        if msg['message']['text'] == '/gandalf':
            send_message(master_id, 'Oh sh@t Gandalf mode activated!')
            print(master_id)

            time.sleep(1)
            keyboard.press_and_release("win+r")
            time.sleep(1)
            keyboard.write("chrome.exe")
            keyboard.press_and_release("enter")
            time.sleep(3)
            keyboard.write(gandalf_link)
            keyboard.press_and_release("enter")
            time.sleep(10)
            keyboard.press_and_release("f")
        #----------------------------------------------------------------------
        
        if msg['message']['text'] == '/ping':
            send_message(master_id, '.')
    #time.sleep(100)