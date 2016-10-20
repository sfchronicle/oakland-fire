import os
from app import app

from views import *

if __name__ == '__main__':
    BASE_DIR = os.path.realpath(os.path.dirname(__file__))

    # Start app
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0')