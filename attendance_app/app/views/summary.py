from flask import Blueprint, render_template, current_app
from ..services.summary_service import get_monthly_summary

summary_bp = Blueprint("summary", __name__)

@summary_bp.route("/summary")
def summary():
    excel_path = current_app.instance_path + "/" + current_app.config["EXCEL_FILENAME"]
    data = get_monthly_summary(
        excel_path,
        current_app.config["EXCEL_SHEET"],
        hourly_rate=current_app.config["HOURLY_RATE"],
        target_salary=current_app.config["TARGET_SALARY"]
    )
    return render_template("summary.html", summary_data=data)
