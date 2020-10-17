from flask import Flask
# from flask_cors import CORS <- Not necessary due to the proxy

# Initialize App
app = Flask(__name__)

if __name__ == '__main__':
    app.run()
