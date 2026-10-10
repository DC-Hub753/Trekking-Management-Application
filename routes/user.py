from datetime import date

from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from models import db, User, Trek, Booking
from config import user_required


# -----------------------------
# User Dashboard
# -----------------------------

@user_required
def user_dashboard():

    available_treks = Trek.query.filter_by(status="Open").all()

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).all()

    booked_treks = []

    for booking in bookings:
        if booking.status == "Booked":
            trek = Trek.query.get(booking.trek_id)
            if trek:
                booked_treks.append(trek)

    return render_template(
        "user/dashboard.html",
        available_treks=available_treks,
        booked_treks=booked_treks
    )

# -----------------------------
# View Available Treks
# -----------------------------

@user_required
def user_treks():

    search = request.args.get("search", "")
    difficulty = request.args.get("difficulty", "")

    query = Trek.query.filter_by(status="Open")

    if search:
        query = query.filter(
            (Trek.name.ilike(f"%{search}%")) |
            (Trek.location.ilike(f"%{search}%"))
        )

    if difficulty:
        query = query.filter_by(difficulty=difficulty)

    treks = query.all()

    return render_template(
        "user/view_treks.html",
        treks=treks,
        search=search,
        difficulty=difficulty
    )


# -----------------------------
# Edit Profile
# -----------------------------

@user_required
def edit_profile():

    user = User.query.get_or_404(
        current_user.id
    )

    if request.method == "POST":

        user.name = request.form["name"]

        user.email = request.form["email"]

        user.phone = request.form["phone"]

        db.session.commit()

        flash(
            "Profile Updated Successfully.",
            "success"
        )

        return redirect(
            url_for("user_dashboard")
        )

    return render_template(
        "user/edit_profile.html",
        user=user
    )


# -----------------------------
# Book Trek
# -----------------------------

@user_required
def book_trek(id):

    trek = Trek.query.get_or_404(id)

    # Prevent duplicate booking

    existing = Booking.query.filter_by(
        user_id=current_user.id,
        trek_id=trek.id
    ).first()

    if existing:

        flash(
            "You have already booked this trek.",
            "warning"
        )

        return redirect(
            url_for("user_treks")
        )

    # Check trek status

    if trek.status != "Open":

        flash(
            "This trek is not currently open for booking.",
            "danger"
        )

        return redirect(
            url_for("user_treks")
        )

    # Check slots

    if trek.slots <= 0:

        flash(
            "No slots available.",
            "danger"
        )

        return redirect(
            url_for("user_treks")
        )

    booking = Booking(

        user_id=current_user.id,

        trek_id=trek.id,

        booking_date=date.today(),

        status="Booked"
    )

    trek.slots -= 1

    db.session.add(booking)

    db.session.commit()

    flash(
        "Trek Booked Successfully!",
        "success"
    )

    return redirect(
        url_for("user_treks")
    )


# -----------------------------
# Cancel Booking
# -----------------------------

@user_required
def cancel_booking(id):

    booking = Booking.query.get_or_404(id)

    if booking.user_id != current_user.id:

        flash(
            "You cannot cancel this booking.",
            "danger"
        )

        return redirect(
            url_for("booking_history")
        )

    if booking.status != "Booked":

        flash(
            "This booking cannot be cancelled.",
            "warning"
        )

        return redirect(
            url_for("booking_history")
        )

    trek = Trek.query.get(
        booking.trek_id
    )

    if trek:

        trek.slots += 1

    booking.status = "Cancelled"

    db.session.commit()

    flash(
        "Booking Cancelled Successfully.",
        "success"
    )

    return redirect(
        url_for("booking_history")
    )


# -----------------------------
# Booking History
# -----------------------------

@user_required
def booking_history():

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).all()

    booking_treks = {}

    for booking in bookings:

        trek = Trek.query.get(
            booking.trek_id
        )

        booking_treks[booking.id] = trek

    return render_template(
        "user/history.html",
        bookings=bookings,
        booking_treks=booking_treks
    )


# -----------------------------
# Route Registration
# -----------------------------

def register_user_routes(app):

    app.add_url_rule(
        "/user/dashboard",
        "user_dashboard",
        user_dashboard
    )

    app.add_url_rule(
        "/user/treks",
        "user_treks",
        user_treks
    )

    app.add_url_rule(
        "/user/profile",
        "edit_profile",
        edit_profile,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/user/book/<int:id>",
        "book_trek",
        book_trek
    )

    app.add_url_rule(
        "/user/cancel/<int:id>",
        "cancel_booking",
        cancel_booking
    )

    app.add_url_rule(
        "/user/history",
        "booking_history",
        booking_history
    )