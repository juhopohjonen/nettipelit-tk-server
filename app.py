from flask import Flask

# Values for development server
USE_DEBUG = True
PORT = 80

app = Flask(__name__)


from views import *

from apis import *

if __name__ == '__main__':
    app.run(debug=USE_DEBUG, port=PORT)


