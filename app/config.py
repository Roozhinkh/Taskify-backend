import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/taskify.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False