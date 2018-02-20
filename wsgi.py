import socket
from time import ctime
from flask import Flask, Response

application = Flask(__name__)
log_path = "/mnt/log"

@application.route("/")
def hello():
    with open(log_path, 'a+') as log_file:
        log_file.write(socket.gethostname() + " " + str(ctime()) + "\n")
        log_file.seek(0)
        data = log_file.read()
    return Response(data, mimetype="text/plain")

if __name__ == "__main__":
    application.run()
