import os


class Config:
    SECRET_KEY = 'c2c73bf04ba3158fedb88947b8eaf8d8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('GMAIL_USER')
    MAIL_PASSWORD = os.environ.get('GMAIL_PW')
    MAIL_USE_TLS = True
