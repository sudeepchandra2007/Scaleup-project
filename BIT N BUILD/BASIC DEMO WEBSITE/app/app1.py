from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models for Startup and Investor
class Startup(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

class Investor(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup/startup', methods=['GET', 'POST'])
def signup_startup():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        user_id = request.form['user_id']
        if Startup.query.get(user_id):
            flash('User ID already exists. Please choose a different one.')
            return redirect(url_for('signup_startup'))
        new_startup = Startup(id=user_id, name=name, phone=phone)
        db.session.add(new_startup)
        db.session.commit()
        flash('Startup signed up successfully!')
        return redirect(url_for('login_startup'))
    return render_template('signup_startup.html')

@app.route('/signup/investor', methods=['GET', 'POST'])
def signup_investor():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        user_id = request.form['user_id']
        if Investor.query.get(user_id):
            flash('User ID already exists. Please choose a different one.')
            return redirect(url_for('signup_investor'))
        new_investor = Investor(id=user_id, name=name, phone=phone)
        db.session.add(new_investor)
        db.session.commit()
        flash('Investor signed up successfully!')
        return redirect(url_for('login_investor'))
    return render_template('signup_investor.html')

@app.route('/login/startup', methods=['GET', 'POST'])
def login_startup():
    if request.method == 'POST':
        user_id = request.form['user_id']
        startup_info = Startup.query.get(user_id)
        if startup_info:
            flash(f"Welcome, {startup_info.name}! Your phone is {startup_info.phone}.")
            return redirect(url_for('home'))
        flash('Invalid credentials. Please try again.')
    return render_template('login_startup.html')

@app.route('/login/investor', methods=['GET', 'POST'])
def login_investor():
    if request.method == 'POST':
        user_id = request.form['user_id']
        investor_info = Investor.query.get(user_id)
        if investor_info:
            flash(f"Welcome, {investor_info.name}! Your phone is {investor_info.phone}.")
            return redirect(url_for('view_startups'))
        flash('Invalid credentials. Please try again.')
    return render_template('login_investor.html')

@app.route('/view_startups')
def view_startups():
    all_startups = Startup.query.all()
    return render_template('view_startups.html', startups=all_startups)

if __name__ == '__main__':
    app.run(debug=True)
