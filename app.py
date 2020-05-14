###################
# Kate Miller
# UNI: khm2125
###################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memes")
def memes():
    return render_template("memes.html")

#start the server
if __name__ == "__main__":
    app.run()