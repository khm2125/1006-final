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
def intro():
    return render_template("index.html")

#start the server
if __name__ == "__main__":
    app.run()