import os
from datetime import datetime, timedelta
from openpyxl import load_workbook
from flask import current_app
from .excel_service import ensure_excel_initialized


def save_input_data(form_data: dict):
    """
    入力フォームからのデータをExcelファイルに保存する

    Parameters:
    form_data (dict): 入力フォームからのデータ
    """

    ensure_excel_initialized()

    date_str = form_data["date"]
    start_str = f"{form_data['start_hour']}:{form_data['start_minute']}"
    end_str = f"{form_data['end_hour']}:{form_data['end_minute']}"
    break_str = form_data.get("break_time", "").strip() or "00:00"

    # 安全なフォーマット補正
    if ":" not in break_str or break_str.startswith(":"):
        break_str = "00:00"
    try:
        break_h, break_m = map(int, break_str.split(":"))
    except ValueError:
        break_h, break_m = 0, 0

    # 実働時間計算
    start_dt = datetime.strptime(f"{date_str} {start_str}", "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(f"{date_str} {end_str}", "%Y-%m-%d %H:%M")
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)

    break_td = timedelta(hours=break_h, minutes=break_m)
    worked_td = end_dt - start_dt - break_td
    worked_str = f"{int(worked_td.total_seconds() // 3600):02d}:{int((worked_td.total_seconds() % 3600) // 60):02d}"

    # Excel に保存
    excel_path = os.path.join(current_app.instance_path, current_app.config["EXCEL_FILENAME"])
    wb = load_workbook(excel_path)
    sheet = wb[current_app.config["EXCEL_SHEET"]]

    sheet.append([
        date_str, start_str, end_str,
        f"{break_h:02d}:{break_m:02d}",
        worked_str,
        form_data["project"],
        form_data["content"],
        False  # 初期状態は報告未チェック
    ])

    wb.save(excel_path)
