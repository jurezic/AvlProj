from flask import Flask, request, Response
from jsonrpcserver import method, dispatch
import sys
import hashlib
"""
inp = sys.stdin.readlines()
hash_func = inp[0].strip()
message = '\n'.join(inp[1:]).strip()

h = hashlib.new(hash_func)
h.update(str.encode(message))

print (h.hexdigest())


class SimpleHasher(jrpc.service.SocketObject):
    @jrpc.service.method
    def hashIt(self, content):
        h = hashlib.new("md5")
        h.update(str.encode(content))
        print(h.hexdigest())
        return h.hexdigest()

if __name__ == "__main__":
    print("Starting server")
    server = SimpleHasher(50001)
    server.run_wait()
"""

app = Flask(__name__)
"""
@method
def ping():
    return "pong"
"""
@method
def ping(content):
    h = hashlib.new("md5")
    h.update(str.encode(content))
    return str(h.hexdigest())

@app.route("/", methods=["POST"])
def index():
    req = request.get_data().decode()
    print(req)
    response = ping(req)
    print(type(response))
    print(response[:32])
    hashed = response[:32]
    return Response(hashed)

if __name__ == "__main__":
    app.run()