from app import create_app

# uv run flask --app attendance_app.app run で実行する場合、
# モジュールレベル変数appが必要なら下記を用意
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)