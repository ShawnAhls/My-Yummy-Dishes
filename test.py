from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # passed

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertTrue(b'You are logged in', response.data)
        # passed

    def test_display_recipes(self):
        tester = app.test_client(self)
        response = tester.get('/display_recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # passed

    def test_add_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipe', follow_redirects=True)
        self.assertTrue(b'You need to Sign in first', response.data)
        # passed

    def test_new_recipe(self):
        tester = app.test_client(self)
        response = tester.post('/new_recipe',
                               data=dict(user="shawn", password="password"),
                               follow_redirects=True)
        self.assertTrue(response.status_code, 200)
        # failed

    def test_edit_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/edit_recipe', follow_redirects=True)
        self.assertTrue(b'You need to Sign in first', response.data)
        # passed

    def test_update_recipe(self):
        tester = app.test_client(self)
        response = tester.post('/update_recipe',
                               data=dict(user="shawn", password="password"),
                               follow_redirects=True)
        self.assertTrue(response.status_code, 200)
        # failed

if __name__ == '__main__':
        unittest.main()