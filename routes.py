from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_jwt_extended import jwt_required

app = Blueprint('app', __name__)


users = {}

@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username  
           
            if 'username' in session:
                flash(f'Hello again, do login!', 'success') 
            else:
                flash(f'Hi {username}, welcome!', 'success')
            return redirect(url_for('app.welcome'))  
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')



@app.route('/welcome')
def welcome():
    username = session.get('username')  
    if not username:
        flash("You must log in first.", "danger")
        return redirect(url_for('app.login'))
    return render_template('welcome.html', username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
        
        elif not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password) or not any(c in "!@#$%^&*()-_=+" for c in password):
            flash('Password must contain at least one uppercase, one lowercase, one number, and one special character.', 'danger')
        elif username in users:
            flash('Username already exists', 'danger')
        else:
            users[username] = password
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('app.login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)  
    flash('You have been logged out.', 'info')  
    return render_template('logout.html') 