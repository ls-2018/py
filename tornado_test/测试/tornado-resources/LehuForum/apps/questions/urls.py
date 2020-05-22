from tornado.web import url

from apps.questions.handlers import QuestionHandler, QuestionDetailHandler, AnswerHandler

urlpattern = [
    url("/questions/", QuestionHandler),
    url("/questions/([0-9]+)/", QuestionDetailHandler),
    url("/questions/([0-9]+)/answers/", AnswerHandler)
]
