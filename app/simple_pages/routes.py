from flask import Blueprint

blueprint = Blueprint('simple_pages', __name__)

@blueprint.get('/')
def index():
  return 'Hello World'
