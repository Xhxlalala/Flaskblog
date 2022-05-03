import os

class Config:
    SECRET_KEY = '###########################'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '邮箱：#######@163.com'
    MAIL_PASSWORD = '授权码：#############'
    MAIL_DEFAULT_SENDER = "Xtar's blog <#######@163.com>"
