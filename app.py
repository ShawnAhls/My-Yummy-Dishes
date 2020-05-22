import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(32)

app.config["MONGO_DBNAME"] = 'myYummyDishes'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00tUser@myfirstcluster-kwp3n.mongodb.net/myYummyDishes?retryWrites=true&w=majority'


mongo = PyMongo(app)

users = mongo.db.users
recipes = mongo.db.recipes


@app.route('/')
@app.route('/home')
def home():
    if 'username' in session:
        flash("You are logged in" + session['user'])
    return render_template('home.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' in session:
        flash('You are already sign in!')
        return redirect(url_for('home'))

    if request.method == 'POST':
        form = request.form.to_dict()

        if form['password'] == form['password1']:
            user = users.find_one({'name': form['username']})
            if user:
                flash(f"{form['username']} already exists!")
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
    else:
        """flash("Passwords dont match!")"""
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if "user" in session:
        user = users.find_one({"name": session['user']})
        if user:
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/auth_user', methods=['GET', 'POST'])
def auth():
    form = request.form.to_dict()
    user = users.find_one({"name": form['username']})
    if user:
        if check_password_hash(user['password'], form['password']):
            session['user'] = form['username']
            return redirect(url_for('home'))
        else:
            flash('Username/Password are not a match')
            return redirect(url_for('login'))
    else:
        flash('You must Register!')
        return redirect(url_for('register'))


@app.route('/sign_out')
def logout():
    session.clear()
    flash('You are now signed out!')
    return redirect(url_for('home'))


@app.route('/display_recipes')
def display_recipes():
    return render_template('display-recipes.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/add_recipe')
def add_recipe():
    if session:
        return render_template('add-recipe.html',
                               all_categories=mongo.db.categories.find())
    else:
        flash('You need Sign in first')
    return redirect(url_for('home'))


@app.route('/new_recipe', methods=["POST"])
def new_recipe():
    new_recipe = {
        'category_name': request.form.get('cartegory_name'),
        'recipe_name': request.form.get('recipe_name'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serving': request.form.get('serving'),
        'username': session['user']
    }
    mongo.db.recipes.insert_one(new_recipe)
    return redirect('display_recipes')


@app.route('/edit_recipe/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if session:
        the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
        all_categories = mongo.db.categories.find()
        category_list = [category for category in all_categories]
        return render_template('edit-recipe.html', recipes=the_recipe,
                               categories=category_list)
    else:
        flash('You need Sign in first')
    return redirect(url_for('home'))


@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update(recipe_id):
    recipes.update({"_id": ObjectId(recipe_id)},
                   {
        'category_name': request.form.get('cartegory_name'),
        'recipe_name': request.form.get('recipe_name'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serving': request.form.get('serving'),
        'username': session['user']
    })
    return redirect(url_for('display_recipes'))


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipes=the_recipe)


@app.route('/delete/<recipe_id>', methods=['GET', 'POST'])
def delete(recipe_id):
    if session:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash('Recipe Deleted')
        return render_template('display-recipes.html')
    else:
        flash('You need Sign in first')
    return redirect(url_for('home'))


@app.route('/categories/')
def categories():
    return render_template('category.html',
                            categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)