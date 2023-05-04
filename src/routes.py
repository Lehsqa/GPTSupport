from flask import request
from flask_restx import Api, Resource, fields
from src.chatGPT import ChatGPT


rest_api = Api(version='1.0', title='QA API')
chat = ChatGPT()


question_model = rest_api.model(
    'QuestionModel', {
        'question': fields.String(required=True)
    }
)


@rest_api.route('/api/question')
class Question(Resource):
    @rest_api.expect(question_model, validate=True)
    def post(self):

        req_data = request.json

        _question = req_data.get('question')

        if _question == "":
            return {
               "error": "true"
            }, 404
        return chat.get_result(_question)
