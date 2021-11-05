from app import app as current_app
import unittest
import sys,os,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class FlaskTest(unittest.TestCase):

    #check if response is 200
    def test_index(self):
        tester = current_app.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #check if content returned is application/json
    def test_index_content(self):
        tester = current_app.test_client(self)
        response = tester.get("/login")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    #check data returned
    def test_index_data(self):
        tester = current_app.test_client(self)
        response = tester.get("/login")
        self.assertEqual(b'Simplii' in response.data, True)

if __name__=="__main__":
     unittest.main()