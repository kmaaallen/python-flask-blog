import os 
import json
from flask import Flask
from flask import render_template
from flask import request
from flask import flash

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route ("/")
def index():
    return render_template("index.html")
    
@app.route ("/about")
def about():
    return render_template("about.html", page_title="About")
    
@app.route ("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {} we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact Us")

@app.route ("/recipes")
def recipes():
    data = []
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("recipes.html", page_title="Recipes", string_list=["Ready", "Steady", "Bake!"], cakes=data)
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
    port = int(os.environ.get("PORT"))),
    debug=True