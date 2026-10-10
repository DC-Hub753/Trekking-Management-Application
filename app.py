import os

from flask import Flask, render_template

from werkzeug.security import generate_password_hash

from models import db, Admin

from config import (
    DB_PATH,
    login_manager
)

from routes.auth import register_auth_routes
from routes.admin import register_admin_routes
from routes.user import register_user_routes
from routes.staff import register_staff_routes


# -----------------------------
# Create Flask App
# -----------------------------

app = Flask(__name__)


# -----------------------------
# Configuration
# -----------------------------

#app.config["SECRET_KEY"] = "TrekkingApp_MAD1_2026_Final"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + DB_PATH
)

app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False


# -----------------------------
# Initialize Database
# -----------------------------

#db.init_app(app)
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

db.init_app(app)

with app.app_context():
    db.create_all()

    # Create initial admin from environment variables
    admin_username = os.environ.get("ADMIN_USERNAME")
    admin_password = os.environ.get("ADMIN_PASSWORD")

    if admin_username and admin_password:
        from werkzeug.security import generate_password_hash
        from models import Admin

        admin = Admin.query.filter_by(
            username=admin_username
        ).first()

        if not admin:
            admin = Admin(
                username=admin_username,
                password=generate_password_hash(admin_password)
            )
            db.session.add(admin)
            db.session.commit()


# -----------------------------
# Initialize Login Manager
# -----------------------------

login_manager.init_app(app)


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# -----------------------------
# Register Routes
# -----------------------------

register_auth_routes(app)

register_admin_routes(app)

register_user_routes(app)

register_staff_routes(app)


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    app.run(debug=False)
