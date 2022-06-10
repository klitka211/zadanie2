from flask import Flask, request
from datetime import datetime
import sys
import os

app = Flask(__name__)
port = 5100

if len(sys.argv) > 1:
    port = sys.argv[1]
print(datetime.now(), "Krzysztof Litka ==== Port : {} ".format(port))



@app.route('/')
def hello():
    date = datetime.now()
    h = f" IP: {request.remote_addr} ====  {date}"
    return h

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
