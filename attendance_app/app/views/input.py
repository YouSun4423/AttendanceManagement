from flask import Blueprint, render_template, request, redirect, current_app
from datetime import date
from ..services.input_service import save_input_data

# attendance_app/app/views/input.py
# 入力フォーム用のBlueprintを定義
# このBlueprintは、日付とプロジェクト名を入力するためのルートを提供する
# 入力データは、Excelファイルに保存される
input_bp = Blueprint("input", __name__)


# 入力フォームのルート
# URL: /
@input_bp.route("/")
def index():
    """
    入力フォームを表示するためのルート

    Returns:
    str: レンダリングされたHTMLテンプレート
    """
    project_path = current_app.instance_path + "/" + current_app.config["PROJECT_FILE"]
    try:
        with open(project_path, encoding="utf-8") as f:
            projects = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        projects = []

    return render_template("input.html", today=date.today().strftime("%Y-%m-%d"), projects=projects)


# 入力データを保存するルート
# URL: /submit
@input_bp.route("/submit", methods=["POST"])
def submit():
    """
    入力データを保存するためのルート

    Returns:
    str: リダイレクト先のURL
    """
    save_input_data(request.form.to_dict())
    return redirect("/")
