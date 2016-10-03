from app import app
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        req = self.app.get('/')
        assert 'ERROR' not in req.data

if __name__ == '__main__':
    unittest.main()
