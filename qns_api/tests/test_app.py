import unittest
import json
from flask import request
from api import create_app
from api import app
from instance.config import TestingConfig
from api.models import questions
from flask import jsonify

#setting my Base URL.
BASE_URL =  'http://127.0.0.1:5000/api/v1/questions'

#class below has methods for unittests of my app.testcase is also created through the subclass.
class QuestionsTestCase(unittest.TestCase):

#method creates the app, initialises the test client and dummy data for the tests.
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.question = questions(
            qnId=1, question= 'What is an algorithm?', answers= ['set of rules', 'set of instructions']
        )
        #self.question = jsonify({'question': question})
#method below tests endpoint to get all questions such that the response is 200 for OK
    def test_get_questions(self):
        with self.client as client:
            response = client.get(BASE_URL, content_type="application/json", data=json.dumps(dict()))
            self.assertEqual(response.status_code,200)

#method below tests endpoint to get a specific question such that the response is 200 for OK
    def test_get_specific_question(self):
        with self.client as client:
            response = client.get(BASE_URL+'/1', content_type='application/json', data=json.dumps(dict(qnId=1)))
            self.assertEqual(response.status_code, 200)

#method below tests endpoint to post a question such that the response is 200 for OK
    def test_post_question(self):
        with self.client as client:
            response = client.post(BASE_URL, content_type='application/json',
            data=json.dumps(dict(question='What is exception handling?')))
            self.assertEqual(response.status_code,200)
#method below tests endpoint to post an answer such that the response is 200 for OK
    def test_post_answer(self):
        with self.client as client:
            response = client.post(BASE_URL+'/1/answers', content_type='application/json',
            data=json.dumps(dict(answer='algorithm is a set of rules')))
            self.assertEqual(response.status_code, 200)
