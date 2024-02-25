from decouple import config as Envron
import os

basedir= os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=Envron("FORM_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'blogpost.db')