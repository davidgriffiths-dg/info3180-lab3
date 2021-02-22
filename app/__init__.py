from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
#app.config['MAIL_SERVER']='smtp.mailtrap.io'
#app.config['MAIL_PORT']=465
#app.config['MAIL_USERNAME']='271d5de9819a28'
#app.config['MAIL_PASSWORD']='a88c4d4ba62bdd'
#app.config['SECRET_KEY']='dgdg123'

mail= Mail(app)
from app import views