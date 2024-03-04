from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Users
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def add_user():
    if request.method == 'POST':
        user = request.form.get('user')
        
        if len(user) < 1:
            flash('Username is too short!', category='error')
        else:
            new_user = Users(user_name=user, email=current_user.email, password=current_user.password, date_created=current_user.date_created, last_login_time=current_user.last_login_time)
            db.session.add(new_user)
            db.session.commit()
            flash('User added!', category='success')
        
    return render_template("home.html", user=current_user)




    

