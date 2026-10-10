from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from models import db, Staff, Trek, Booking
from config import staff_required


# -----------------------------
# Staff Dashboard
# -----------------------------

@staff_required
def staff_dashboard():

    treks = Trek.query.filter_by(
        staff_id=current_user.id
    ).all()

    trek_data = []

    for trek in treks:

        registered_users = Booking.query.filter_by(
            trek_id=trek.id,
            status="Booked"
        ).count()

        trek_data.append({
            "trek": trek,
            "registered_users": registered_users
        })

    return render_template(
        "staff/dashboard.html",
        trek_data=trek_data
    )


# -----------------------------
# Assigned Treks
# -----------------------------

@staff_required
def staff_treks():

    treks = Trek.query.filter_by(
        staff_id=current_user.id
    ).all()

    return render_template(
        "staff/assigned_treks.html",
        treks=treks
    )


# -----------------------------
# Update Trek
# -----------------------------

@staff_required
def update_trek(id):

    trek = Trek.query.get_or_404(id)

    # Only assigned staff can update

    if trek.staff_id != current_user.id:

        flash(
            "You are not assigned to this trek.",
            "danger"
        )

        return redirect(
            url_for("staff_treks")
        )

    if request.method == "POST":

        trek.slots = int(
            request.form["slots"]
        )

        trek.status = request.form["status"]

        db.session.commit()

        flash(
            "Trek Updated Successfully",
            "success"
        )

        return redirect(
            url_for("staff_treks")
        )

    return render_template(
        "staff/update_trek.html",
        trek=trek
    )


# -----------------------------
# Participants
# -----------------------------

@staff_required
def participants(id):

    trek = Trek.query.get_or_404(id)

    # Only assigned staff can view participants

    if trek.staff_id != current_user.id:

        flash(
            "You are not assigned to this trek.",
            "danger"
        )

        return redirect(
            url_for("staff_treks")
        )

    bookings = Booking.query.filter_by(
        trek_id=id
    ).all()

    return render_template(
        "staff/participants.html",
        bookings=bookings
    )


# -----------------------------
# Edit Staff Profile
# -----------------------------

@staff_required
def edit_staff_profile():

    staff = Staff.query.get_or_404(
        current_user.id
    )

    if request.method == "POST":

        staff.name = request.form["name"]

        staff.email = request.form["email"]

        staff.phone = request.form["phone"]

        db.session.commit()

        flash(
            "Profile Updated Successfully.",
            "success"
        )

        return redirect(
            url_for("staff_dashboard")
        )

    return render_template(
        "staff/edit_profile.html",
        staff=staff
    )


# -----------------------------
# Route Registration
# -----------------------------

def register_staff_routes(app):

    app.add_url_rule(
        "/staff/dashboard",
        "staff_dashboard",
        staff_dashboard
    )

    app.add_url_rule(
        "/staff/treks",
        "staff_treks",
        staff_treks
    )

    app.add_url_rule(
        "/staff/update/<int:id>",
        "update_trek",
        update_trek,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/staff/participants/<int:id>",
        "participants",
        participants
    )

    app.add_url_rule(
        "/staff/profile",
        "edit_staff_profile",
        edit_staff_profile,
        methods=["GET", "POST"]
    )