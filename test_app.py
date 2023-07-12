import unittest
import xmlrunner

from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, Flask!')

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'This is the about page.')

    # def test_user(self):
    #     # Test with a regular username
    #     username = 'John'
    #     response = self.app.get(f'/user/{username}')
    #     self.assertEqual(response.status_code, 200)
    #     expected_message = f"Welcome, {username}!"
    #     self.assertEqual(response.data.decode(), expected_message)

    #     # Test with a username containing special characters
    #     special_username = '@#User123!'
    #     response = self.app.get(f'/user/{special_username}')
    #     self.assertEqual(response.status_code, 200)
    #     expected_message = f"Welcome, {special_username}!"
    #     self.assertEqual(response.data.decode(), expected_message)

    # def test_multiply(self):
    #     # Test with positive numbers
    #     num1 = 5
    #     num2 = 10
    #     response = self.app.get(f'/multiply/{num1}/{num2}')
    #     self.assertEqual(response.status_code, 200)
    #     expected_message = f"The multiplication of {num1} and {num2} is: 50"
    #     self.assertEqual(response.data.decode(), expected_message)

    #     # Test with negative numbers
    #     num1 = -5
    #     num2 = 10
    #     response = self.app.get(f'/multiply/{num1}/{num2}')
    #     self.assertEqual(response.status_code, 200)
    #     expected_message = f"The multiplication of {num1} and {num2} is: -50"
    #     self.assertEqual(response.data.decode(), expected_message)

    def test_capitalize(self):
        # Test with a lowercase text
        text = 'hello, world!'
        response = self.app.get(f'/capitalize/{text}')
        self.assertEqual(response.status_code, 200)
        expected_message = "The capitalized text is: HELLO, WORLD!"
        self.assertEqual(response.data.decode(), expected_message)

        # Test with an already capitalized text
        text = 'HELLO, WORLD!'
        response = self.app.get(f'/capitalize/{text}')
        self.assertEqual(response.status_code, 200)
        expected_message = "The capitalized text is: HELLO, WORLD!"
        self.assertEqual(response.data.decode(), expected_message)

    def test_invalid_route(self):
        response = self.app.get('/invalid_route')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)

if __name__ == '__main__':
    # Configure the test runner with XML output
    runner = xmlrunner.XMLTestRunner(output='xunit-reports')

    # Discover and run the tests with the configured runner
    unittest.main(testRunner=runner)
