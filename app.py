from flask import Flask
from gevent import pywsgi


app = Flask(__name__, static_folder='static', static_url_path='')

if __name__ == '__main__':
    http_server = pywsgi.WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()

    # app.run(host="0.0.0.0", port=80)

