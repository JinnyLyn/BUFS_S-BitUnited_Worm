from flask import Flask, request
from os import urandom
from subprocess import run, TimeoutExpired

app = Flask(__name__)
app.secret_key = urandom(32)

try:
    FLAG = open("/flag", "r").read().strip()
except:
    FLAG = "[**FLAG**]"

ALLOWED_HOSTS = ['dreamhack.io', 'tools.dreamhack.io']

@app.route("/api/v1/test/curl", methods=["POST"])
def admin():
    url = request.form["url"].strip()
    for host in ALLOWED_HOSTS:
        if url.startswith('http://' + host):
            break

        return {'result': False, 'msg': 'Not Allowed host'}
    
    if url.endswith('/test/internal'):
        return {'result': False, 'msg': 'Not Allowed endpoint'}

    try:
        response = run(
            ["curl", f"{url}"], capture_output=True, text=True, timeout=1
        )
        return {'result': True, 'msg': response.stdout}

    except TimeoutExpired:
        return {'result': False, 'msg': 'Timeout'}


@app.route('/api/v1/test/internal', methods=["GET"])
def test():
    ip = request.remote_addr
    if not ip == '127.0.0.1':
        return {'result': False, 'msg': 'Only local access is allowed'}
    return {'result': True, 'msg': FLAG}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')