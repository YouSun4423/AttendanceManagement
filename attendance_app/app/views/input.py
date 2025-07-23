from flask import Blueprint, render_template, request, redirect, current_app
from datetime import date
from ..services.input_service import save_input_data

input_bp = Blueprint("input", __name__)

@input_bp.route("/")
def index():
    project_path = current_app.instance_path + "/" + current_app.config["PROJECT_FILE"]
    try:
        with open(project_path, encoding="utf-8") as f:
            projects = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        projects = []

    return render_template("input.html", today=date.today().strftime("%Y-%m-%d"), projects=projects)

@input_bp.route("/submit", methods=["POST"])
def submit():
    save_input_data(request.form.to_dict())
    return redirect("/")
