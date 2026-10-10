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

app.config["SECRET_KEY"] = "TrekkingApp_MAD1_2026_Final"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + DB_PATH
)

app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False


# -----------------------------
# Initialize Database
# -----------------------------

db.init_app(app)


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

    with app.app_context():

        import os

        os.makedirs(
            "instance",
            exist_ok=True
        )

        db.create_all()

        # Create default Admin only once

        admin = Admin.query.filter_by(
            username="admin"
        ).first()

        if not admin:

            admin = Admin(

                username="admin",

                password=generate_password_hash(
                    "admin123"
                )
            )

            db.session.add(admin)

            db.session.commit()

            print(
                "✅ Default Admin Created"
            )

        else:

            print(
                "✅ Admin Already Exists"
            )

    app.run(debug=False)