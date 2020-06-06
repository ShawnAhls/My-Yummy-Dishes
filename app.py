import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.urandom(32)

app.config["MONGO_DBNAME"] = 'myYummyDishes'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


mongo = PyMongo(app)

users = mongo.db.users
recipes = mongo.db.recipes
categories = mongo.db.categories


@app.route('/')
@app.route('/home')
def home():

    """ Loads the home page and indicates which user is logged in """

    if 'user' in session:
        flash("You are signed in as " + session['user'])
    return render_template('home.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/register', methods=['GET', 'POST'])
def register():

    # Registration for users

    if 'user' in session:
        flash('You are already sign in!')
        return redirect(url_for('home'))

    if request.method == 'POST':
        form = request.form.to_dict()

        # Check if user exists

        if form['password'] == form['password1']:
            user = users.find_one({'name': form['username']})
            if user:
                flash('{form["username"]} already exists!')

            # If user does not exist, user can create new account and an encoded password

            else:
                hash_pass = generate_password_hash(form['password'])
                users.insert_one({
                                'name': form['username'],
                                'password': hash_pass
                                })
                user = users.find_one({"name": form['username']})
            if user:
                session['user'] = user['name']
                return redirect(url_for('home'))

    # An error will prompt the user if the password dont match

        else:
            flash("Passwords dont match!")
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    # Registered users can login

    if "user" in session:
        user = users.find_one({"name": session['user']})
        if user:
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/auth_user', methods=['GET', 'POST'])
def auth():

    # When user logs in and authenticates the user with the correcct password

    form = request.form.to_dict()
    user = users.find_one({"name": form['username']})
    if user:

        # Unhashes the password to check if the correct password was used

        if check_password_hash(user['password'], form['password']):
            session['user'] = form['username']
            return redirect(url_for('home'))
        else:

            # If not, an error will appear informing the user

            flash('Username/Password are not a match')
            return redirect(url_for('login'))
    else:
        flash('You must Register!')
        return redirect(url_for('register'))


@app.route('/sign_out')
def logout():
    session.clear()
    flash('You are now signed out! ' + ' Good bye')
    return redirect(url_for('home'))


@app.route('/recipes/<category_id>')
def display_recipes(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})["category_name"]
    recipe_name = mongo.db.recipes.find({"category_name": category})
    return render_template('display-recipes.html',
                           recipes=recipe_name,
                           categories=category)


@app.route('/recipes/display/<category_name>')
def display_recipes_name(category_name):
    recipe_name = mongo.db.recipes.find({"category_name": category_name})
    return render_template('display-recipes.html',
                           recipes=recipe_name)


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipes=the_recipe,
                           categories=mongo.db.categories.find())
# @app.route('/recipes')
# def display_recipes():
#     categories = mongo.db.categories.find()
#     recipes = mongo.db.recipes.find()
#     category_name = [category for category in categories]
#     recipe_name = [recipe for recipe in recipes]
#     return render_template('display-recipes.html',
#                            categories=category_name,
#                            recipes=recipe_name)


@app.route('/recipe/add', methods=["GET"])
def add_recipe():

    # Allows the logged in users to add a new recipe

    if 'user' in session:
        categories = mongo.db.categories.find()
        category_list = [category for category in categories]
        return render_template('add-recipe.html',
                               categories=category_list)
    else:
        flash('You need to Sign in first')
    return redirect(url_for('home'))


@app.route('/recipe/new', methods=["POST"])
def new_recipe():

    # Adds a new recipe to the database

    new_recipe = {
        'category_name': request.form.get('category_name'),
        'recipe_name': request.form.get('recipe_name'),
        'recipe_image': request.form.get('recipe_image'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serving': request.form.get('serving'),
        'username': session['user']
    }
    mongo.db.recipes.insert_one(new_recipe)
    return redirect(url_for('home'))


@app.route('/recipe/edit/<recipe_id>', methods=["GET"])
def edit_recipe(recipe_id):

    # The user can edit their recipe

    if 'user' in session:
        the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
        category = mongo.db.categories.find()
        return render_template('edit-recipe.html', recipes=the_recipe,
                               categories=category)
    else:
        flash('You need to Sign in first')
    return redirect(url_for('home'))


@app.route('/recipe/update/<recipe_id>', methods=["POST"])
def update(recipe_id):

    # Lets the user update the edited recipe

    the_recipe = mongo.db.recipes.update({"_id": ObjectId(recipe_id)},
                                         {
        'category_name': request.form.get('category_name'),
        'recipe_name': request.form.get('recipe_name'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serving': request.form.get('serving'),
        'username': session['user']
    })

    return redirect(url_for('recipe', recipes=the_recipe))


@app.route('/delete/<recipe_id>', methods=['GET', 'POST'])
def delete(recipe_id):

    # The user of the recipe delete the recipe

    if 'user' in session:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash('Recipe Deleted')
        return redirect(url_for('display_recipes'))
    else:
        flash('You need to Sign in first')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
#os.environ.get('DEBUG')
