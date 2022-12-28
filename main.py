from flask import Flask
from views import main_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=18000)