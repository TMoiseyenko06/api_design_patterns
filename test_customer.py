import unittest
from unittest.mock import MagicMock, patch
from app import app

class customerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        patch('utils.util.verify_token',return_value = None).start()
        patch('utils.util.verify_role',return_value=None).start()
        self.mock_db = MagicMock()
        patch('app.db',self.mock_db).start()

    def tearDown(self):
        patch.stopall()
        
    def test_add(self):
        payload = {'name':"tim","email":"wedgfwg","phone":"2673564671"}
        response = self.app.post('/customer/',json=payload)
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_remove(self):
        
        response = self.app.delete('/customer/1')
        print(response.data)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()