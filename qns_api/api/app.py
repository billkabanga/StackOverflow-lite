from flask import Flask, request, jsonify, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
my_blue_print = Blueprint('qns_bp',__name__, url_prefix='/api/v1')
api = Api(my_blue_print)

questions = [
    {
        'qnId': 1,
        'question': 'What is an algorithm',
        'answers': [
            {
                'answer': 'algorithm is'
            }
        ]
    }
]

class questions_handler(Resource):
    def get(self):
        return jsonify({'questions': questions})

api.add_resource(questions_handler, '/questions')
