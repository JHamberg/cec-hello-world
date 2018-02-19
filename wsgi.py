import socket
from flask import Flask

application = Flask(__name__)
log_path = "/mnt/log"

@application.route("/")
def hello():
    with open(log_path) as f:
        data = f.readLines()
    return data

if __name__ == "__main__":
    application.run()
    with open(log_path, "w") as f:
        f.write(socket.gethostname() + " " + time.time())

