from flask import Flask, request, jsonify, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)

#For versioning purposes, i initialise my blueprint with a name and a url prefix
my_blue_print = Blueprint('qns_bp',__name__, url_prefix='/api/v1')

#Below i make my blueprint an instance of class Api
api = Api(my_blue_print)

#for incrementing, i set qnId to 1.
qnId = 1

#Initialisation of my data. a list of questions with lists of answers.
questions = [
    {
        'qnId': qnId ,
        'question': 'What is an algorithm',
        'answers': [
            {
                'answer': 'algorithm is'
            }
        ]
    }
]

#class below has endpoints for the general questions list.
class questions_handler(Resource):
    def get(self):
        return jsonify({'questions': questions})
    
    def post(self):
        request_data = request.get_json()
        new_question = {
            'qnId': qnId + 1,
            'question': request_data['question'],
            'answers': []
        }
        questions.append(new_question)
        return jsonify(new_question)

api.add_resource(questions_handler, '/questions')

#class below has an endpoint for a specific question
class specific_qn(Resource):
    def get(self, qnId):
        for question in questions:
            if question['qnId'] == qnId:
                return jsonify(question)
        return jsonify({'message': 'question does not exist'})

api.add_resource(specific_qn, '/questions/<int:qnId>')

#class below has an endpoint for posting an answer
class add_answer(Resource):
    def post(self,qnId):
        request_data = request.get_json()
        for question in questions:
            if question['qnId'] == qnId:
                new_answer = {
                    'answer': request_data['answer']
                }
                question['answers'].append(new_answer)
                return jsonify(new_answer)
        return jsonify({'message': 'question not found'})

api.add_resource(add_answer, '/questions/<int:qnId>/answers')

