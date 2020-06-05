from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Test the dipplay of the home page

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # passed

    # Test home to display a message when the user is signed in

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertTrue(b'You are logged in', response.data)
        # passed

    # Test the user can register

    def test_register(self):
        tester = app.test_client(self)
        response = tester.post('/register',
                               data=dict(username="name",
                                         password="password",
                                         password1="password"),
                               follow_redirects=True)
        self.assertTrue(response.status_code, 200)
        # passed with a keyerror on line 52

    # Test the user can Sign in

    def test_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username="shawn", password="password"),
                               follow_redirects=True)
        self.assertTrue(response.status_code, 200)
        # passed

    # Test the user can Sign in with incorrecct details

    def test_auth_user(self):
        tester = app.test_client(self)
        response = tester.post('/auth_user',
                               data=dict(username="wrong", password="wrong"),
                               follow_redirects=True)
        self.assertTrue(b'Username/Password are not a match', response.data)
        # passed with a keyerror on line 95

    # Test the user can Sign out

    def test_sign_out(self):
        tester = app.test_client(self)
        tester.post('/login',
                    data=dict(user="shawn", password="password"),
                    follow_redirects=True)
        response = tester.get('/sign_out')
        self.assertTrue(b'You are now signed out!', response.data)
        # passed

    # Test to display all the recipes in the category

    def test_recipes(self):
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # failed

    # Test add recipe to display a message if user is not signed in

    def test_add_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipe', follow_redirects=True)
        self.assertTrue(b'You need to Sign in first', response.data)
        # passed

    # The user and password are for a user in the users database, to test new recipe

    def test_new_recipe(self):
        tester = app.test_client(self)
        response = tester.post('/new_recipe',
                               data=dict(user="shawn", password="password"),
                               follow_redirects=True)
        self.assertTrue(response.status_code, 200)
        # passes

    # Test edit recipe to display a message if user is not signed in

    def test_edit_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/edit_recipe', follow_redirects=True)
        self.assertTrue(b'You need to Sign in first', response.data)
        # passed

    # The user and password are for a user in the users database, to test update recipe

    def test_update_recipe(self):
        tester = app.test_client(self)
        response = tester.post('/update_recipe',
                               data=dict(user="shawn", password="password"),
                               follow_redirects=True)
        self.assertTrue(response.status_code, 200)
        # passed

    # Test to display a recipe
    """
    def test_recipe_id(self):
        tester = app.test_client(self)
        response = tester.get('/recipe_id', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    """


if __name__ == '__main__':
    unittest.main()
