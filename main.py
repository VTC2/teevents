from flask import Flask
from flask import request
from flask import render_template

teventapp = Flask(__name__)

@teventapp.route('/')
def main():
    return render_template("main.html")

if __name__ == '__main__':
    teventapp.run(host="localhost", port=80)