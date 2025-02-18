import requests
from flask import Blueprint, render_template
from app.config import API_URL, API_KEY

blueprint = Blueprint('cookies', __name__)

@blueprint.get('/cookies')
def cookies():
  response = requests.get(url=f'{API_URL}/api/cookies?key={API_KEY}')
  cookies = response.json()

  return render_template('cookies/index.html', cookies=cookies)
