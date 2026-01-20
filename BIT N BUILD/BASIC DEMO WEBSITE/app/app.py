from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory storage for demo purposes
startups = {}
investors = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup/startup', methods=['GET', 'POST'])
def signup_startup():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        user_id = request.form['user_id']
        if user_id in startups:
            flash('User ID already exists. Please choose a different one.')
            return redirect(url_for('signup_startup'))
        startups[user_id] = {'name': name, 'phone': phone}
        flash('Startup signed up successfully!')
        return redirect(url_for('login_startup'))
    return render_template('signup_startup.html')

@app.route('/signup/investor', methods=['GET', 'POST'])
def signup_investor():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        user_id = request.form['user_id']
        if user_id in investors:
            flash('User ID already exists. Please choose a different one.')
            return redirect(url_for('signup_investor'))
        investors[user_id] = {'name': name, 'phone': phone}
        flash('Investor signed up successfully!')
        return redirect(url_for('login_investor'))
    return render_template('signup_investor.html')

@app.route('/login/startup', methods=['GET', 'POST'])
def login_startup():
    if request.method == 'POST':
        user_id = request.form['user_id']
        if user_id in startups:
            startup_info = startups[user_id]
            flash(f"Welcome, {startup_info['name']}! Your phone is {startup_info['phone']}.")
            return redirect(url_for('home'))
        flash('Invalid credentials. Please try again.')
    return render_template('login_startup.html')

@app.route('/login/investor', methods=['GET', 'POST'])
def login_investor():
    if request.method == 'POST':
        user_id = request.form['user_id']
        if user_id in investors:
            investor_info = investors[user_id]
            flash(f"Welcome, {investor_info['name']}! Your phone is {investor_info['phone']}.")
            return redirect(url_for('view_startups'))
        flash('Invalid credentials. Please try again.')
    return render_template('login_investor.html')

@app.route('/view_startups')
def view_startups():
    return render_template('view_startups.html', startups=startups)

if __name__ == '__main__':
    app.run(debug=True)
