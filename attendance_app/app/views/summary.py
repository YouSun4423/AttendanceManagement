from flask import Blueprint, render_template, current_app
from ..services.summary_service import get_monthly_summary

# attendance_app/app/views/summary.py
# サマリ表示用のBlueprintを定義
# このBlueprintは、月次のサマリを表示するためのルートを提供する
# サマリデータは、Excelファイルから取得される
summary_bp = Blueprint("summary", __name__)


# サマリ表示のルート
# URL: /summary
@summary_bp.route("/summary")
def summary():
    """
    月次サマリを表示するためのルート

    Returns:
    str: レンダリングされたHTMLテンプレート"""

    excel_path = current_app.instance_path + "/" + current_app.config["EXCEL_FILENAME"]
    data = get_monthly_summary(
        excel_path,
        current_app.config["EXCEL_SHEET"],
        hourly_rate=current_app.config["HOURLY_RATE"],
        target_salary=current_app.config["TARGET_SALARY"]
    )
    return render_template("summary.html", summary_data=data)
