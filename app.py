from flask import Flask, render_template, request
from flask_login import login_required, current_user
from views import ethereum, home, bitcoin

app = Flask(__name__)

class ConfigClass(object):
    SECRET_KEY="DPMC01R4F43LF0D4*¨F$%&ÖPDKLÇSJããâÃldas´p"
    WTF_CSRF_SECRET_KEY="4 C4R4LH4 D4 S3NH4! C5RF    d~ç]12]~ç321]~ç21]3]~çtrwe]t~r4ç3]çt]34#"
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'rrafaelrribeiro@gmail.com'
    MAIL_PASSWORD = ''

    # # Flask-User settings

    # USER_APP_NAME = "Trace Labs"
    # USER_ENABLE_EMAIL = True        
    # USER_ENABLE_USERNAME = True    
    # USER_ENABLE_INVITATION = True
    # #USER_REQUIRE_INVITATION = True
    # USER_EMAIL_SENDER_NAME = USER_APP_NAME
    # USER_EMAIL_SENDER_EMAIL = ""
    # USER_ENABLE_REGISTER = True

    # REMEMBER_COOKIE_NAME = False
    # USER_ENABLE_REMEMBER_ME = False
    # USER_ENABLE_FORGOT_PASSWORD = True
    # # USER_ENABLE_CHANGE_PASSWORD = True
    # # USER_ENABLE_FORGOT_PASSWORD = True

app.config.from_object(__name__+'.ConfigClass')
app.register_blueprint(ethereum.ethereum_bp)
app.register_blueprint(home.home_bp)
app.register_blueprint(bitcoin.bitcoin_bp)
