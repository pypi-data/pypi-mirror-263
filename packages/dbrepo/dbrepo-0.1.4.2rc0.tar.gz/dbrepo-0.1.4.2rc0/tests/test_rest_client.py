import unittest

from client.RestClient import RestClient


class DatabaseTest(unittest.TestCase):

    def test_constructor(self):
        # test
        client = RestClient()
        self.assertIsNone(client.username)
        self.assertIsNone(client.password)

    def test_constructor_credentials_succeeds(self):
        # test
        client = RestClient(username='admin', password='pass')
        self.assertEqual('admin', client.username)
        self.assertEqual('pass', client.password)

    def test_wrapper_credentials_succeeds(self):
        # test
        client = RestClient(username='admin', password='pass')
        self.assertEqual('admin', client.username)
        self.assertEqual('pass', client.password)


if __name__ == "__main__":
    unittest.main()
