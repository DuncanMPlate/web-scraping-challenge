import scrape_mars
from flask import Flask, render_template, redirect
import pymongo


# Create an instance of Flask
app = Flask(__name__)
connection_url = "mongodb://localhost:27017/mars_db"
# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")
mongo = pymongo.MongoClient(connection_url)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    mars_data = mongo.mars_db.mars.find_one()
    # Return template and data
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    result=scrape_mars.scrape_info()
    mongo.mars_db.mars.update({}, result, upsert=True)
    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)