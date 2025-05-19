from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"Welcome! Message: {os.getenv('WELCOME_MSG', 'Hello from Flask!')}"

@app.route('/status')
def status():
    return {'status': 'OK', 'ip': request.remote_addr}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
