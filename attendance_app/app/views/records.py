from flask import Blueprint, render_template, request, redirect, current_app
from ..services.record_service import get_monthly_records, update_reported_flags

records_bp = Blueprint("records", __name__)

@records_bp.route("/records")
def records():
    excel_path = current_app.instance_path + "/" + current_app.config["EXCEL_FILENAME"]
    records_by_month = get_monthly_records(excel_path, current_app.config["EXCEL_SHEET"])
    return render_template("records.html", records_by_month=records_by_month)

@records_bp.route("/update_reported", methods=["POST"])
def update_reported():
    update_reported_flags(request.form)
    return redirect("/records")
