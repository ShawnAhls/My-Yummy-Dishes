import os
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = os.urandom(32)

app.config["MONGO_DBNAME"] = 'myYummyDishes'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00tUser@myfirstcluster-kwp3n.mongodb.net/myYummyDishes?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=4, max=25)])
    email = StringField('Email Address', validators=[DataRequired(),
                        Length(min=6, max=35)])
    password = PasswordField('New Password', [
                             validators.DataRequired(),
                             validators.EqualTo('confirm',
                             message='Passwords must match')])
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Thanks for registering {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/display_recipes')
def display_recipes():
    return render_template('display-recipes.html',
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())



"""
@app.route('/display_recipes_cat/<category_id>')
def display_recipes_cat(category_id):
    all_categories = mongo.db.categories.find({'category_id': category_id})
    return render_template('display-recipes.html', categories=all_categories)
"""


@app.route('/add_recipe')
def add_recipe():
    all_categories = mongo.db.categories.find()
    category_list = [category for category in all_categories]
    return render_template('add-recipe.html',
                           categories=category_list)


@app.route('/new_recipe', methods=["POST"])
def new_recipe():
    new_recipe = {
        'category_name': request.form.get('cartegory_name'),
        'recipe_name': request.form.get('recipe_name'),
        'ingredients_description': request.form.get('ingredients_description'),
        'method_instruction': request.form.get('method_instruction'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serving': request.form.get('serving')
    }
    mongo.db.recipes.insert_one(new_recipe)
    return redirect('display_recipes')


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    category_list = [category for category in all_categories]
    return render_template('edit-recipe.html', recipes=the_recipe,
                           categories=category_list)


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


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipes=the_recipe)


@app.route('/delete/<recipe_id>', methods=['GET', 'POST'])
def delete(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    return redirect(url_for('display_recipes'))


@app.route('/categories/')
def categories():
    return render_template('category.html',
                           categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)