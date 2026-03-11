# 🦟 ระบบจัดการข้อมูลมาสไรเดอร์ (Kamen Rider Database)

ระบบจัดการข้อมูลมาสไรเดอร์ทุกยุคสมัย พัฒนาด้วย **Django + PostgreSQL** พร้อม Deploy บน **Render.com**



  ฟีเจอร์หลัก

 เพิ่ม / แก้ไข / ลบ / แสดงข้อมูลมาสไรเดอร์
 บันทึกความสามารถพิเศษ พร้อม Power Level
  บันทึกประวัติการต่อสู้ (ชนะ/แพ้/เสมอ)
  ค้นหาและกรองตามยุค (โชวะ / เฮเซ / เรวะ)
  Form Validation ป้องกันข้อมูลผิดพลาด
  รองรับ PostgreSQL บน Render.com








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



 MasRider
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

CompetitionHistory
| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|--------|----------|
| rider | ForeignKey | มาสไรเดอร์ |
| opponent | CharField | คู่ต่อสู้ |
| event_name | CharField | ชื่อเหตุการณ์ |
| event_date | DateField | วันที่ |
| result | CharField | ผล (win/lose/draw) |

 Ability
| ฟิลด์ | ประเภท | คำอธิบาย |
|-------|--------|----------|
| rider | ForeignKey | มาสไรเดอร์ |
| name | CharField | ชื่อความสามารถ |
| power_level | PositiveIntegerField | ระดับพลัง 1-100 |
| description | TextField | คำอธิบาย |

---


