# 🦟 ระบบจัดการข้อมูลมาสไรเดอร์ (Kamen Rider Database)

ระบบจัดการข้อมูลมาสไรเดอร์ทุกยุคสมัย พัฒนาด้วย **Django + PostgreSQL** พร้อม Deploy บน **Render.com**

---

##  ฟีเจอร์หลัก

-  เพิ่ม / แก้ไข / ลบ / แสดงข้อมูลมาสไรเดอร์
-  บันทึกความสามารถพิเศษ พร้อม Power Level
-  บันทึกประวัติการต่อสู้ (ชนะ/แพ้/เสมอ)
-  ค้นหาและกรองตามยุค (โชวะ / เฮเซ / เรวะ)
-  Form Validation ป้องกันข้อมูลผิดพลาด
-  รองรับ PostgreSQL บน Render.com

---

## 🛠️ การติดตั้งบนเครื่อง (Local Development)

```bash
# 1. Clone โปรเจค
git clone https://github.com/YOUR_USERNAME/masrider-project.git
cd masrider-project

# 2. สร้าง Virtual Environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. ติดตั้ง Dependencies
pip install -r requirements.txt

# 4. รัน Migrations
python manage.py migrate

# 5. (ตัวเลือก) โหลดข้อมูลตัวอย่าง
python manage.py loaddata masrider/fixtures/sample_data.json

# 6. สร้าง Admin User
python manage.py createsuperuser

# 7. รันเซิร์ฟเวอร์
python manage.py runserver
```

เปิดเบราว์เซอร์ไปที่: http://127.0.0.1:8000

---

## 🚀 การ Deploy บน Render.com

### ขั้นตอนที่ 1: Push ขึ้น GitHub

```bash
git init
git add .
git commit -m "Initial commit: Kamen Rider Database System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/masrider-project.git
git push -u origin main
```

### ขั้นตอนที่ 2: สร้าง PostgreSQL บน Render

1. ไปที่ https://render.com → **New** → **PostgreSQL**
2. ตั้งชื่อ: `masrider-db`
3. กด **Create Database**
4. คัดลอก **Internal Database URL**

### ขั้นตอนที่ 3: Deploy Web Service

1. **New** → **Web Service**
2. เชื่อม GitHub repo ของคุณ
3. ตั้งค่าดังนี้:

| ฟิลด์ | ค่า |
|-------|-----|
| **Name** | masrider-app |
| **Runtime** | Python 3 |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn masrider_project.wsgi:application` |

4. เพิ่ม **Environment Variables**:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | (กด Generate) |
| `DEBUG` | `False` |
| `DATABASE_URL` | (วาง Internal Database URL) |

5. กด **Create Web Service**

### ขั้นตอนที่ 4: สร้าง Admin User บน Render

ใน Render Dashboard → Shell:
```bash
python manage.py createsuperuser
```

---

## 📁 โครงสร้างโปรเจค

```
masrider-project/
├── masrider/                  # Django App หลัก
│   ├── models.py              # Database Models
│   ├── views.py               # Logic การแสดงผล
│   ├── forms.py               # Form + Validation
│   ├── urls.py                # URL Routing
│   ├── admin.py               # Django Admin
│   ├── fixtures/
│   │   └── sample_data.json   # ข้อมูลตัวอย่าง
│   └── templates/masrider/    # HTML Templates
├── masrider_project/          # Django Settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── build.sh                   # Render build script
├── render.yaml                # Render config
└── manage.py
```

---

## 🗄️ Database Schema

### MasRider
| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|--------|----------|
| name | CharField | ชื่อจริง |
| alias | CharField | ชื่อมาสไรเดอร์ |
| age | PositiveIntegerField | อายุ |
| series | CharField | ยุค (showa/heisei/reiwa) |
| organization | CharField | องค์กร |
| transformation_device | CharField | อุปกรณ์แปลงร่าง |
| abilities | TextField | ความสามารถ |
| bio | TextField | ประวัติ |

### CompetitionHistory
| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|--------|----------|
| rider | ForeignKey | มาสไรเดอร์ |
| opponent | CharField | คู่ต่อสู้ |
| event_name | CharField | ชื่อเหตุการณ์ |
| event_date | DateField | วันที่ |
| result | CharField | ผล (win/lose/draw) |

### Ability
| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|--------|----------|
| rider | ForeignKey | มาสไรเดอร์ |
| name | CharField | ชื่อความสามารถ |
| power_level | PositiveIntegerField | ระดับพลัง 1-100 |
| description | TextField | คำอธิบาย |

---

## 🔗 Links

- **GitHub**: https://github.com/YOUR_USERNAME/masrider-project
- **Live Demo**: https://masrider-app.onrender.com
