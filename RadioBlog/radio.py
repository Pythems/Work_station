from flask import Flask,render_template,url_for,flash,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager,login_required
import forms
import models

app= Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cae17c7a36edbe90977e9d33af090957'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site2.db'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return models.User.get_id

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = models.User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/pick_up", methods=['GET', 'POST'])
def pick_up():
    form = forms.PickUpForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        pickup = models.Pickup(username=form.username.data, location=form.location.data, trip=form.trip.data)
        db.session.add(pickup)
        db.session.commit()
        flash('Nearest driver to your location will pick you up at your location', 'success')
        return redirect(url_for('pick_up'))
    return render_template('pick_up.html', title='Pick Up', form=form)

@app.route("/bookings", methods=['GET', 'POST'])
def bookings():
    form = forms.BookForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # user = models.User(username=form.username.data, email=form.email.data, password=hashed_password)
        terminal = models.Terminal(username=form.username.data,trip_date=form.trip_date.data,destination=form.destination.data)

        db.session.add(terminal)
        db.session.commit()
        flash('Your booking has been saved', 'success')
        return redirect(url_for('home'))
    return render_template('bookings.html', title='Pick Up', form=form)



if __name__== '__main__':
	app.run(debug=True)