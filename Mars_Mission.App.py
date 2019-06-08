from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Scrape_to_Mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars = mongo.db.mars
    mars_data = Scrape_to_Mars
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"


if __name__ == "__main__":
    app.run(debug=True)
