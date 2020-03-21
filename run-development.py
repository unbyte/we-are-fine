"""
Development Server
"""
from flask_cors import CORS

from app import app

if __name__ == '__main__':
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.run(
        debug=app.config['DEBUG'],
        host=app.config['LISTEN_HOST_DEV'],
        port=app.config['LISTEN_PORT_DEV']
    )
