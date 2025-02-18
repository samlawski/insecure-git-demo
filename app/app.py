from flask import Flask

def create_app():
  app = Flask(__name__)

  register_blueprints(app)

  return app

# Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(simple_pages.routes.blueprint)

  return True