from flask import render_template, request, redirect, url_for, flash

from models import db, User, Staff, Trek, Booking
from config import admin_required


# -----------------------------
# Admin Dashboard
# -----------------------------

@admin_required
def admin_dashboard():

    total_users = User.query.count()

    total_staff = Staff.query.count()

    total_treks = Trek.query.count()

    total_bookings = Booking.query.count()

    return render_template(
        "admin/dashboard.html",

        total_users=total_users,

        total_staff=total_staff,

        total_treks=total_treks,

        total_bookings=total_bookings
    )


# -----------------------------
# Add Trek
# -----------------------------

@admin_required
def add_trek():

    if request.method == "POST":

        from datetime import datetime

        duration = int(
            request.form["duration"]
        )

        slots = int(
            request.form["slots"]
        )

        start_date = datetime.strptime(
            request.form["start_date"],
            "%Y-%m-%d"
        )

        end_date = datetime.strptime(
            request.form["end_date"],
            "%Y-%m-%d"
        )

        if duration <= 0:

            flash(
                "Duration must be greater than 0.",
                "danger"
            )

            return redirect(
                url_for("add_trek")
            )

        if slots < 0:

            flash(
                "Available slots cannot be negative.",
                "danger"
            )

            return redirect(
                url_for("add_trek")
            )

        if end_date < start_date:

            flash(
                "End date cannot be before start date.",
                "danger"
            )

            return redirect(
                url_for("add_trek")
            )

        trek = Trek(

            name=request.form["name"],

            location=request.form["location"],

            difficulty=request.form["difficulty"],

            duration=duration,

            slots=slots,

            start_date=start_date,

            end_date=end_date
        )

        db.session.add(trek)

        db.session.commit()

        flash(
            "Trek Added Successfully",
            "success"
        )

        return redirect(
            url_for("admin_dashboard")
        )

    return render_template(
        "admin/add_trek.html"
    )


# -----------------------------
# View Treks
# -----------------------------

@admin_required
def view_treks():

    search = request.args.get(
        "search",
        ""
    )

    if search:

        if search.isdigit():

            treks = Trek.query.filter(
                (Trek.id == int(search)) |
                (Trek.name.ilike(f"%{search}%")) |
                (Trek.location.ilike(f"%{search}%"))
            ).all()

        else:

            treks = Trek.query.filter(
                (Trek.name.ilike(f"%{search}%")) |
                (Trek.location.ilike(f"%{search}%"))
            ).all()

    else:

        treks = Trek.query.all()

    return render_template(
        "admin/view_treks.html",
        treks=treks,
        search=search
    )


# -----------------------------
# Edit Trek
# -----------------------------

@admin_required
def edit_trek(id):

    trek = Trek.query.get_or_404(id)

    if request.method == "POST":

        trek.name = request.form["name"]

        trek.location = request.form["location"]

        trek.difficulty = request.form["difficulty"]

        trek.duration = int(
            request.form["duration"]
        )

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
            url_for("view_treks")
        )

    return render_template(
        "admin/edit_trek.html",
        trek=trek
    )


# -----------------------------
# Delete Trek
# -----------------------------

@admin_required
def delete_trek(id):

    trek = Trek.query.get_or_404(id)

    db.session.delete(trek)

    db.session.commit()

    flash(
        "Trek Deleted Successfully",
        "success"
    )

    return redirect(
        url_for("view_treks")
    )


# -----------------------------
# View Staff
# -----------------------------

@admin_required
def view_staff():

    search = request.args.get(
        "search",
        ""
    )

    if search:

        if search.isdigit():

            staffs = Staff.query.filter(
                (Staff.id == int(search)) |
                (Staff.name.ilike(f"%{search}%")) |
                (Staff.email.ilike(f"%{search}%"))
            ).all()

        else:

            staffs = Staff.query.filter(
                (Staff.name.ilike(f"%{search}%")) |
                (Staff.email.ilike(f"%{search}%"))
            ).all()

    else:

        staffs = Staff.query.all()

    return render_template(
        "admin/view_staff.html",
        staffs=staffs,
        search=search
    )


# -----------------------------
# Approve Staff
# -----------------------------

@admin_required
def approve_staff(id):

    staff = Staff.query.get_or_404(id)

    staff.approved = True

    db.session.commit()

    flash(
        "Staff Approved Successfully",
        "success"
    )

    return redirect(
        url_for("view_staff")
    )


# -----------------------------
# Blacklist Staff
# -----------------------------

@admin_required
def blacklist_staff(id):

    staff = Staff.query.get_or_404(id)

    staff.blacklisted = True

    db.session.commit()

    flash(
        "Staff Blacklisted",
        "danger"
    )

    return redirect(
        url_for("view_staff")
    )


# -----------------------------
# Assign Staff
# -----------------------------

@admin_required
def assign_staff(id):

    staff = Staff.query.get_or_404(id)

    treks = Trek.query.all()

    if request.method == "POST":

        trek = Trek.query.get(
            request.form["trek_id"]
        )

        trek.staff_id = staff.id

        db.session.commit()

        flash(
            "Staff Assigned Successfully",
            "success"
        )

        return redirect(
            url_for("view_staff")
        )

    return render_template(
        "admin/assign_staff.html",
        staff=staff,
        treks=treks
    )


# -----------------------------
# View Users
# -----------------------------

@admin_required
def view_users():

    search = request.args.get(
        "search",
        ""
    )

    if search:

        if search.isdigit():

            users = User.query.filter(
                (User.id == int(search)) |
                (User.name.ilike(f"%{search}%")) |
                (User.email.ilike(f"%{search}%"))
            ).all()

        else:

            users = User.query.filter(
                (User.name.ilike(f"%{search}%")) |
                (User.email.ilike(f"%{search}%"))
            ).all()

    else:

        users = User.query.all()

    return render_template(
        "admin/view_users.html",
        users=users,
        search=search
    )


# -----------------------------
# Blacklist User
# -----------------------------

@admin_required
def blacklist_user(id):

    user = User.query.get_or_404(id)

    user.is_blacklisted = True

    db.session.commit()

    flash(
        "User Blacklisted Successfully",
        "danger"
    )

    return redirect(
        url_for("view_users")
    )


# -----------------------------
# View Bookings
# -----------------------------

@admin_required
def view_bookings():

    bookings = Booking.query.all()

    return render_template(
        "admin/view_bookings.html",
        bookings=bookings
    )


# -----------------------------
# Route Registration
# -----------------------------

def register_admin_routes(app):

    app.add_url_rule(
        "/admin/dashboard",
        "admin_dashboard",
        admin_dashboard
    )

    app.add_url_rule(
        "/admin/add-trek",
        "add_trek",
        add_trek,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/admin/treks",
        "view_treks",
        view_treks
    )

    app.add_url_rule(
        "/admin/edit-trek/<int:id>",
        "edit_trek",
        edit_trek,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/admin/delete-trek/<int:id>",
        "delete_trek",
        delete_trek
    )

    app.add_url_rule(
        "/admin/staff",
        "view_staff",
        view_staff
    )

    app.add_url_rule(
        "/admin/approve-staff/<int:id>",
        "approve_staff",
        approve_staff
    )

    app.add_url_rule(
        "/admin/blacklist-staff/<int:id>",
        "blacklist_staff",
        blacklist_staff
    )

    app.add_url_rule(
        "/admin/assign-staff/<int:id>",
        "assign_staff",
        assign_staff,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/admin/users",
        "view_users",
        view_users
    )

    app.add_url_rule(
        "/admin/blacklist-user/<int:id>",
        "blacklist_user",
        blacklist_user
    )

    app.add_url_rule(
        "/admin/bookings",
        "view_bookings",
        view_bookings
    )