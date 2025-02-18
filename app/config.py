from dotenv import load_dotenv
from os import environ

load_dotenv()

API_URL = 'https://hackable-api.vercel.app'
API_KEY = environ.get('API_KEY')