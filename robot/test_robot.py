import requests
from dotenv import load_dotenv
import os

load_dotenv() #Load .env variables
api_token = os.getenv("API_TOKEN") #Get token api from .env file
chat_id = os.getenv("CHAT_ID") #Get chat id from .env file

def send_to_telegram(message, apiToken, chatID):

    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

def send_photo(chatID, file_opened, apiToken):
    telegramToken = apiToken
    api_url=f'https://api.telegram.org/bot{telegramToken}/'
    method = "sendPhoto"
    params = {'chat_id': chatID}
    files = {'photo': file_opened}
    resp = requests.post(api_url + method, params, files=files)
    return resp

send_to_telegram(message="Hola desde python!", apiToken=api_token, chatID=chat_id)
send_photo(chatID=chat_id, apiToken=api_token, file_opened=open('./robot/test.png', 'rb'))