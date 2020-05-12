import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myYummyDishes'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00tUser@myfirstcluster-kwp3n.mongodb.net/myYummyDishes?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/display_recipes')
def display_recipes():
    return render_template('display-recipes.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/display_recipes_cat/<category_name>', methods=['GET', 'POST'])
def display_recipes_cat(category_name):
    results = mongo.db.recipes.find({'category_name': category_name})
    return render_template('display-recipes.html', recipes=results)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    add_recipe = request.form.get('recipe_name'),
    mongo.db.recipes.insert({'recipe_name': add_recipe})
    return render_template('add-recipe.html',
                           recipes=mongo.db.recipes.find())


@app.route('/edit_recipe')
def edit_recipe():
    return render_template('edit-recipe.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/recipe')
def recipe():
    instruction = ['1. Heat a splash of vegetable oil in a hot pan. Season the steak with salt and pepper, then put in the hot pan. Cook for 2-3 minutes on each side (for medium-rare) until the outside is brown and starting to crisp at the edges, then set aside on a warm plate to rest',
                   '2. Return the pan to the heat and add a large knob of butter along with the chopped anchovy fillets and capers. Stir to heat through and scrape up any crispy bits from the base of the pan.',
                   '3. Return the steak to the pan along with any resting juices and spoon the hot butter over to coat. Top with a knob of fresh butter and serve with chips, watercress and your favourite mustard.']
    return render_template('recipe.html', instruction=instruction,
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/categories')
def categories():
    return render_template('category.html',
                           categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)