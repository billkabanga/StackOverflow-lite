from flask import Flask, request, jsonify, Blueprint,make_response
from flask_restful import Resource, Api


#For versioning purposes, i initialise my blueprint with a name and a url prefix
my_blue_print = Blueprint('qns_bp',__name__, url_prefix='/api/v1')

#Below i make my blueprint an instance of class Api
api = Api(my_blue_print)

#Initialisation of my data. an empty list.
questions = []


#class below has endpoints for the general questions list.
class questions_handler(Resource):
    def get(self):
        if len(questions) == 0:
            return jsonify({'message': 'No questions have been posted so far'})
        return jsonify({'questions': questions})
    
    def post(self):
        request_data = request.get_json()
        #for incrementing qnId basing on length of questions list.
        qnId = len(questions) + 1
        new_question = {
            'qnId': qnId,
            'question': request_data['question'],
            'answers': []
        }
        if isinstance(request_data['question'], str):
            questions.append(new_question)
            return make_response(jsonify({'message':'Question has been added'}),201)
        return make_response(jsonify({'message':'Invalid input'}),406)

api.add_resource(questions_handler, '/questions')

#class below has an endpoint for a specific question
class specific_qn(Resource):
    def get(self, qnId):
        for question in questions:
            if question['qnId'] == qnId:
                return jsonify(question)
        return make_response(jsonify({'message': 'question not found'}),404)
   
api.add_resource(specific_qn, '/questions/<int:qnId>')

#class below has an endpoint for posting an answer
class add_answer(Resource):
    def post(self,qnId):
        request_data = request.get_json()
        for question in questions:
            if question['qnId'] == qnId:
                new_answer = request_data['answers']
                question['answers'].append(new_answer)
                return make_response(jsonify({'message':'Answer has been added'}),201)
        return make_response(jsonify({'message': 'question not found'}),404)

api.add_resource(add_answer, '/questions/<int:qnId>/answers')

