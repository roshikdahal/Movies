from flask import Flask
from Movies.logger import logging
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "starting flask app"


if __name__ == "__main__":
    logging.info("we are testing..")
    app.run( debug = True )