
import unittest
from unittest.mock import MagicMock, patch
from app import app

class customerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.mock_db = MagicMock()
        patch('app.db',self.mock_db).start()
        patch('controllers.customerController.token_required', lambda f: f).start()
        
        
    def test_add(self):
        payload = {'name':"tim","email":"wedgfwg","phone":"2673564671"}
        response = self.app.post('/customer/',json=payload)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()