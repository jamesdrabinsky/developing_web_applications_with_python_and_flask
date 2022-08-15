import logging
from logging.handlers import RotatingFileHandler

from flask import (Flask, escape, flash, redirect, render_template, request,
                   session, url_for)
from flask.logging import default_handler
from pydantic import BaseModel, ValidationError, validator

app = Flask(__name__)

# Import the blueprints
from project.stocks import stocks_blueprint
from project.users import users_blueprint

# Register the blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')

# Logging configuration
app.logger.removeHandler(default_handler)

file_handler = RotatingFileHandler(
    "flask-stock-portfolio.log", maxBytes=16384, backupCount=20
)
file_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]"
)
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info("Starting the Flask Stock Portfolio App")

app.secret_key = b"\t\xf4\x800\xc2s\xd1b\x9bgu\x10\xf1}Ol\xff\xda\x84L\x17\xd9\xb52\xfd\nf\xda\x96\x9f~\xb5"
