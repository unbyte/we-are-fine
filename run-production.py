"""
Running Script for Production Use
using WSGI in gEvent
"""

if __name__ == '__main__':
    from app import app
    from gevent.pywsgi import WSGIServer

    listen_address = (
        app.config['LISTEN_HOST_PRODUCTION'],
        app.config['LISTEN_PORT_PRODUCTION']
    )

    server = WSGIServer(listen_address, app)
    server.serve_forever()
