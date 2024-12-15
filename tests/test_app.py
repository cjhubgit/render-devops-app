import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):  # Changed 'Self' to 'self'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Changed 'Self' to 'self'
        self.assertIn(b"Welcome to Render CI/CD Pipeline!", response.data)  # Ensure this matches your app's output

if __name__ == '__main__':  # Corrected indentation
    unittest.main()   