import requests
from flask import Blueprint

blueprint = Blueprint('cookies', __name__)

@blueprint.get('/cookies')
def cookies():
  return 'Cookies'
