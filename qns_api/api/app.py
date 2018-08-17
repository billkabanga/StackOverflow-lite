from flask import Flask, request, jsonify

app = Flask(__name__)

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