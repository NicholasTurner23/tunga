from decouple import config as Envron

class Config:
    SECRET_KEY=Envron("FORM_SECRET_KEY")