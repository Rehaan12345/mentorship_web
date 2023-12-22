from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
import random
import smtplib
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

views = Blueprint("views", __name__)  

@views.route("/", methods=["GET", "POST"])
def home():
    return render_template("layout.html")