import socket
from time import ctime
from flask import Flask

application = Flask(__name__)
log_path = "/mnt/log"

@application.route("/")
def hello():
    with open(log_path, 'a+') as file:
        file.write(socket.gethostname() + " " + str(ctime()) + "\n")
        file.seek(0)
        data = file.read()
    return Response(data, mimetype="text/plain")

if __name__ == "__main__":
    application.run()
