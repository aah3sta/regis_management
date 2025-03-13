from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from datetime import datetime
from .database import get_db, Student 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user, login_user

routes = Blueprint('routes', __name__)

@routes.route('/home', methods=['GET', 'POST'])
@routes.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    #add login logic
    db = get_db()
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        student = db.query(Student).filter(Student.email == email).first()
        print(student.email, 'welcome girllll')
        if student:
            if student.password == password:
                if check_password_hash(student.password, password):
                    print('Login Successful')
                    login_user(student, remember=True)
                    session['firstname'] = student.firstname
                    return redirect(url_for('routes.student_dasboard'))
                else:
                    flash('Incorrect Password')
                    print('Incorrect Password')
            else:
                flash('Student Not Found')
                print('Student Not Found')
    return render_template('login.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    #add signup logic
    db = get_db()
    if request.method == "POST":
        password = request.form['password']
        hashedpassword = generate_password_hash(password, method='scrypt', salt_length=8)
        print(password, hashedpassword)
        new_student = Student(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            email=request.form['email'],
            password=hashedpassword,
        )  

        db.add(new_student)
        db.commit()
    return render_template('signup.html')

@routes.route('/student_dashboard', methods=['GET', 'POST'])
@login_required
def student_dashboard():
    firstname = session['firstname']
    return render_template('student_dashboard.html', firstname = firstname)

@routes.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))