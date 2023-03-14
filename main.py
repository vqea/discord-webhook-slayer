import requests
import colorama
import os
from colorama import Fore

def SlayWH(url):
    payload = {
        "content": 'WebhookSlayer slayed your webhook!'
    }
    for x in range(15):
        requests.post(url, json=payload)

    requests.delete(url)
    
    print('Slayed Webhook!')
    exit(0)

def SpamWH(url):
    payload = {
        "content": 'WebhookSlayer slayed your webhook!'
    }
    try:
        while True:
            requests.post(url, json=payload)
    except KeyboardInterrupt:
        print('Spammer has been stopped!')
        await asyncio.sleep(5)
        main()
    
def deleteWH(url):
    requests.delete(url)
    print("Deleted webhook!")
    exit(0)
    
c = Fore.CYAN

def main():
    intro = f"""{c}
  {c}╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═ ╔═╗╦  ╔═╗╦ ╦╔═╗╦═╗
  {c}║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗ ╚═╗║  ╠═╣╚╦╝║╣ ╠╦╝
  {c}╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩ ╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═
  {c}[1]{c} Slay Webhook
  {c}[2]{c} Spam Webhook
  {c}[3]{c} Delete Webhook
  {c}[4]{c} Exit
    """

    os.system('clear')
    print(intro)
    optionx = input("Option: ")
    if optionx == '1':
        try:
            webhookurl = input("Webhook URL: ")
            src = requests.get(webhookurl)
            if src.status_code == 200:
                print("Slaying webhook..")
                SlayWH(webhookurl)
            else:
                print('Invalid webhook')
                await asyncio.sleep(3)
                main()
        except Exception:
            print('Invalid link')
            await asyncio.sleep(3)
            main()
            
    elif optionx == '2':
        try:
            webhookurl = input("Webhook URL: ")
            src = requests.get(webhookurl)
            if src.status_code == 200:
                print("Spamming webhook..")
                SpamWH(webhookurl)
            else:
                print('Invalid webhook')
                await asyncio.sleep(3)
                main()
        except Exception:
            print('Invalid link.')
            await asyncio.sleep(3)
            main()
            
    elif optionx == '3':
        try:
            webhookurl = input("Webhook URL: ")
            src = requests.get(webhookurl)
            if src.status_code == 200:
                print("Deleting webhook..")
                deleteWH(webhookurl)
            else:
                print('Invalid webhook')
                await asyncio.sleep(3)
                main()
        except Exception:
            print('Invalid link')
            await asyncio.sleep(3)
            main()
            
    elif optionx == '4':
        print('Exiting..')
        exit(0)
    
    else:
      main()
