from flask import Flask, redirect, url_for, render_template, session
from flask_dance.contrib.google import make_google_blueprint, google
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///history.db"
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    history = db.relationship("History", backref="user")

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(200))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Google OAuth
blueprint = make_google_blueprint(
    client_id="YOUR_GOOGLE_CLIENT_ID",
    client_secret="YOUR_GOOGLE_CLIENT_SECRET",
    redirect_to="google_login"
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/google_login")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    email = resp.json()["email"]

    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html", user=current_user)
