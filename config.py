import os

class Config:
    SECRET_KEY = 'thisisasecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///crime_reports.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
