from wtforms import StringField, TextAreaField
from wtforms.validators import AnyOf, DataRequired, Length
from wtforms_tornado import Form


class QuestionForm(Form):
    category = StringField("类别", validators=[
        AnyOf(values=["Django专题", "Tornado专题", "Flask专题", "Python专题", "Element专题", "PyTorch专题"])])
    title = StringField("标题", validators=[DataRequired(message="请输入标题"),
                                          Length(min=3, max=200, message="标题长度在3-200之间")])
    content = TextAreaField("问题内容", validators=[DataRequired(message="请输入问题内容")])


class AnswerForm(Form):
    content = TextAreaField("答案内容", validators=[DataRequired(message="请输入回答内容")])
