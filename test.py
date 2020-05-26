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
        response = tester.get('/add_recipe', content_type='html/text')
        self.assertIn(response.status_code, 200)
        self.assertTrue(b'You are logged in', response.data)
        # passed

if __name__ == '__main__':
        unittest.main()