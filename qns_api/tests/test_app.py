import unittest
import json
from flask import request
from qns_api.api import create_app
from qns_api.api import app
from qns_api.instance.config import TestingConfig
from qns_api.api.models import questions
from flask import jsonify

#setting my Base URL.
BASE_URL =  'http://127.0.0.1:5000/api/v1/questions'


#class below has methods for unittests of my app.testcase is also created through the subclass.
class QuestionsTestCase(unittest.TestCase):

#method creates the app, initialises the test client and dummy data for the tests.
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        
        
#method below tests endpoint to get all questions such that the response is a message since no questions have been posted yet.
    def test_empty_questions_list(self):
        with self.client as client:
            response = client.get(BASE_URL,json=dict())
            response_json= json.loads(response.data.decode())
            self.assertIn('No questions have been posted so far', response_json['message'])
#method below tests endpoint to get all questions such that the response is 200 for OK          
    def test_get_questions(self):
        with self.client as client:
            client.post(BASE_URL,json=dict(qnId=1,question='What is an algorithm?',answers=[]))
            response = client.get(BASE_URL)
            self.assertEqual(response.status_code,200)

#method below tests endpoint to get a specific question such that the response is 200 for OK
    def test_get_specific_question(self):
        with self.client as client:
            response = client.get(BASE_URL+'/1',json=dict(qnId=1))
            self.assertEqual(response.status_code, 200)

    def test_get_specific_question_not_existing(self):
        with self.client as client:
            response = client.get(BASE_URL+'/5',json=dict(qnId=1))
            self.assertEqual(response.status_code,404)


#method below tests endpoint to post a question such that the response is 201 for created and 406 for Wrong input
    def test_post_question(self):
        with self.client as client:
            response = client.post(BASE_URL,json=dict(question='What is exception handling?',
            answers=['this is the handling of unique situations']))
            self.assertEqual(response.status_code,201)
    
    def test_invalid_question_posted_integer(self):
        with self.client as client:
            response = client.post(BASE_URL,json=dict(question=4656))
            self.assertEqual(response.status_code,406)  

    def test_invalid_question_posted_spaces(self):
        with self.client as client:
            response = client.post(BASE_URL,json=dict(question='    '))
            self.assertEqual(response.status_code,406)  

    def test_invalid_question_posted_space(self):
        with self.client as client:
            response = client.post(BASE_URL,json=dict(question=''))
            self.assertEqual(response.status_code,406)  



#method below tests endpoint to post an answer such that the response is 201 for created
    def test_post_answer(self):
        with self.client as client:
            client.post(BASE_URL,json=dict(question='What is exception handling?',answers=['this is the handling of unique situations']))
            response = client.post(BASE_URL+'/1/answers',json=dict(answers='set of'))
            self.assertEqual(response.status_code,201)

    def test_question_not_found_for_post_answer(self):
        with self.client as client:
            client.post(BASE_URL,json=dict(question='What is exception handling?',answers=['this is the handling of unique situations']))
            response = client.post(BASE_URL+'/789/answers',json=dict(answers='set of'))
            self.assertEqual(response.status_code,404)

    def test_invalid_posted_answer_spaces(self):
        with self.client as client:
            client.post(BASE_URL,json=dict(question='What is exception handling?',answers=['this is the handling of unique situations']))
            response = client.post(BASE_URL+'/1/answers',json=dict(answers='     '))
            self.assertEqual(response.status_code,406)

    def test_invalid_posted_answer_space(self):
        with self.client as client:
            client.post(BASE_URL,json=dict(question='What is exception handling?',answers=['this is the handling of unique situations']))
            response = client.post(BASE_URL+'/1/answers',json=dict(answers=''))
            self.assertEqual(response.status_code,406)

