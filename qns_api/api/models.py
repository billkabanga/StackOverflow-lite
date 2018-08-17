from flask import jsonify


class questions(object):
    def __init__(self, qnId, question, answers):
        self.qnId = qnId
        self.question = question
        self.answers = answers

    def get_questions(self):
        questions = [
            {
                'qnId': self.qnId,
                'question': self.question,
                'answers': self.answers
            }
        ]
        return jsonify({'questions': questions})

