import service1.entrypoint as server
import service2.entrypoint2 as client
import unittest
import sys
MD5 = 81
URL = 'https://www.python.org'

class TestApp(unittest.TestCase):

    def testDeployOfServer(self):
        self.app = server.app.test_client()
        self.app.testing = True

    def testCommunication(self):
        self.app = server.app.test_client()
        test_string = "I'm a testing string!"
        hashed_string = server.hashIt(test_string)
        assert type(hashed_string) == str

    def testDeployOfClient(self):
        test_download = client.downloadWebsite(URL)
        assert type(test_download) == bytes

    def testHashIt(self):
        self.app = server.app.test_client()
        test_string = "I'm a testing string!"
        hashed_string = server.hashIt(test_string)
        assert sys.getsizeof(hashed_string) == 81

if __name__=='__main__':
    unittest.main()