import socket
from time import ctime
from flask import Flask

application = Flask(__name__)
log_path = "/mnt/log"

@application.route("/")
def hello():
    with open(log_path, 'a+') as f:
        f.write(socket.gethostname() + " " + str(ctime()) + "\n")
        f.seek(0)
        data = f.read()
    return data

if __name__ == "__main__":
    application.run()
