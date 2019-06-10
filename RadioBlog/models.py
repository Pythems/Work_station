from radio import db
# from flask_login import UserMixin

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    # image_file = db.Column(db.String(20),nullable=False, default= 'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    terminal = db.relationship('Terminal', backref='author',lazy=True)

    def __repr__(self):
        # return f"User('{self.username}','{self.email}','{self.image_file}','{self.password}')"
        return f"User('{self.username}','{self.email}','{self.password}')"

class Terminal(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    trip_date = db.Column(db.Text,nullable=False)
    destination = db.Column(db.Text,nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.content}')"

class Pickup(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    location = db.Column(db.Text,nullable=False)
    trip = db.Column(db.Text,nullable=False)
    
    def __repr__(self):
        return f"Post('{self.username}','{self.location}','{self.trip}')"
