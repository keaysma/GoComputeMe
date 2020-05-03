from flask import Flask, send_from_directory, Response
from flask_cors import CORS
from os import system
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload/<content>')
def upload_mock(content):
    with open('USERSOURCE/temp.cpp'.format(content), 'w') as f:
        f.write(content)
    system('em++ USERSOURCE/temp.cpp -O2 -s WASM=1 -s SIDE_MODULE=1 -s EXPORTED_FUNCTIONS="[\'compute\']" -o BINARIES/temp.wasm')
    return 'Upload complete of {}'.format(content)

@app.route('/load/<content>')
def download_mock(content):
    return send_from_directory('BINARIES', '{}.wasm'.format(content), mimetype='application/wasm')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000', debug = True)