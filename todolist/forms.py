from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class ItemForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired(), Length(1,30)])
    submit = SubmitField('添加')


class CompleteAndDeleteForm(FlaskForm):
    complete = SubmitField('转为已办事项')
    delete = SubmitField('删除')


class EditItemForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired(message="数据不能为空！"), Length(1, 30, message="数据长度不在1至30之间")])
    submit = SubmitField('提交')