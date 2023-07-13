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
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskTestCase)

    # Configure the test runner with XML output
    runner = xmlrunner.XMLTestRunner(output='xunit-reports')

    # Run the test suite with the configured runner
    result = runner.run(suite)
