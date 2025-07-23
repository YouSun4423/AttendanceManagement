from flask import Blueprint, render_template, request, redirect, current_app
from ..services.record_service import get_monthly_records, update_reported_flags

# attendance_app/app/views/records.py
# レコード表示用のBlueprintを定義
# このBlueprintは、月次のレコードを表示するためのルートを提供
# レコードデータは、Excelファイルから取得される
records_bp = Blueprint("records", __name__)


# レコード表示のルート
# URL: /records
@records_bp.route("/records")
def records():
    """
    月次レコードを表示するためのルート

    Returns:
    str: レンダリングされたHTMLテンプレート
    """
    excel_path = current_app.instance_path + "/" + current_app.config["EXCEL_FILENAME"]
    records_by_month = get_monthly_records(excel_path, current_app.config["EXCEL_SHEET"])
    return render_template("records.html", records_by_month=records_by_month)


# レコードの報告フラグを更新するルート
# URL: /records/update_reported
@records_bp.route("/update_reported", methods=["POST"])
def update_reported():
    """
    レコードの報告フラグを更新するためのルート

    Returns:
    str: リダイレクト先のURL
    """
    update_reported_flags(request.form)
    return redirect("/records")
