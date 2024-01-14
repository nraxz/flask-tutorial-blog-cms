import os


class Config:
    SECRET_KEY = '06a72e3c0f68f5c929f683d89ce5b1e6'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flaskdb'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
