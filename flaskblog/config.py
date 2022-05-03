import os

class Config:
    SECRET_KEY = '66294800a89b651b6fb0293af3823f76'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'xhx_mail@163.com'
    MAIL_PASSWORD = 'RITTFFYSVMDUAXZI'
    MAIL_DEFAULT_SENDER = "Xtar's blog <xhx_mail@163.com>"