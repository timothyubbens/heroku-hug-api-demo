'''
Test app.py test_api()
'''

import hug
import app
import unittest

class APITest(unittest.TestCase):
    ''' Run unit tests against the update_target_status method '''

    def setUp(self):
        ''' Setup mocked data '''

    def tearDown(self):
        ''' Destroy mocked data '''

class TestWithGoodV1UsersRequest(APITest):
    ''' Test that v1 resource returns nothing useful '''
    def runTest(self):
        ''' Execute test '''
        assert hug.test.get(app, 'v1/users', {'user_id': '123'}).data == 'I do nothing useful.'
