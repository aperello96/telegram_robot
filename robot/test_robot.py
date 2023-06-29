import requests
from dotenv import load_dotenv
import os

load_dotenv() #Load .env variables

def send_to_telegram(message):

    apiToken = os.getenv("API_TOKEN") #Get token api from .env file
    chatID = os.getenv("CHAT_ID") #Get chat id from .env file
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Hola desde python!")