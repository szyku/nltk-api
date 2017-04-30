import os
from gevent.wsgi import WSGIServer
from nltk_api.application import app


def main():
    port = int(os.environ['APP_PORT'])

    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()
    pass


if __name__ == '__main__':
    main()
