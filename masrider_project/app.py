from flask import Flask
import psycopg2

app = Flask(__name__)


DATABASE_URL = "postgresql://masrider_db_user:r3bPJ29oh1pNqiXi3WwBgeqLIxlpbhwC@dpg-d6oiq8ngi27c73ef992g-a.oregon-postgres.render.com/masrider_db"

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        time = cur.fetchone()
        cur.close()
        conn.close()
        return f"เชื่อมต่อ Database สำเร็จ! เวลาใน DB คือ {time}"
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {e}"


if __name__ == "__main__":
    app.run(debug=True)