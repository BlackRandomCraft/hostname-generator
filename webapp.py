from cli import get_hostname_web as get_hostname
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Enter of hostnames you need after slash. Number must be positive!"

@app.route("/<int:num>")
def hostnames(num):
    if num <=0:
        return "Number of hostnames must be positive!"
    return get_hostname(num)

if __name__ == "__main__":
    app.run()
