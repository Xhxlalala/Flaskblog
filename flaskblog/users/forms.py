from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    # DataRequired -- 数据不为空 Length -- 最短为2最长为20
    username = StringField('用户名',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('邮箱',
                         validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',
                                      validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    # def validate_field(self, field):
    #     if True:
    #         raise  ValidationError('Validation Message')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise  ValidationError('用户名已存在')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise  ValidationError('该邮箱已被注册')


class LoginForm(FlaskForm):
    email = StringField('邮箱',
                         validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')


class UpdateAccountForm(FlaskForm):
    username = StringField('用户名',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('邮箱',
                         validators=[DataRequired(), Email()])
    picture = FileField('头像', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('更新')

    # def validate_field(self, field):
    #     if True:
    #         raise  ValidationError('Validation Message')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise  ValidationError('用户名已存在')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise  ValidationError('该邮箱已被注册')


class RequestResetForm(FlaskForm):
    email = StringField('邮箱',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('请求重置密码')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise  ValidationError('该邮箱未注册，请先注册')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('重置密码')