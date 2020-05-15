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
    return render_template('home.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/display/recipes')
def display_recipes():
    return render_template('display-recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/display_recipes_cat/<category_id>')
def display_recipes_cat(category_id):
    all_categories = mongo.db.categories.find({'category_id': category_id})
    return render_template('display-recipes.html', categories=all_categories)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    add_recipe = request.form.get('recipe_name')
    mongo.db.recipes.insert({'recipe_name': add_recipe})
    return render_template('add-recipe.html',
                           recipes=mongo.db.recipes.find())


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit-recipe.html', recipes=the_recipe,
                           categories=all_categories)


@app.route('/recipe/update/<recipe_id>', methods=['POST'])
def update(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
                   {
        'category_name': request.form.get['cartegory_name'],
        'recipe_name': request.form.get['recipe_name'],
        'ingredients_description': request.form.get['ingredients_description'],
        'method_instruction': request.form.get['method_instruction'],
        'prep_time': request.form.get['prep_time'],
        'cooking_time': request.form.get['cooking_time'],
        'serving': request.form.get['serving']
    })
    return redirect(url_for('display_recipes'))


@app.route('/recipe')
def recipe():
    return render_template('recipe.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/delete/<recipe_id>', methods=['GET', 'POST'])
def delete(recipe_id):
    mongo.db.recipes.remove({'recipe_id': ObjectId()})
    return redirect('recipe.html')


@app.route('/categories/')
def categories():
    return render_template('category.html',
                           categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)