โปรแกรม Python ขนาดเล็กที่ช่วยแปลข้อความที่คุณเลือกไว้ในหน้าจอ โดยเพียงแค่กด **ปุ่มลัด (Hotkey)**  
ระบบจะทำการจำลอง Ctrl+C ให้อัตโนมัติ แปลข้อความ และแสดงผลแบบหน้าต่างลอยขนาดเล็กใกล้ตำแหน่งเมาส์

---

## 🧠 ความสามารถ

- ✅ แปลข้อความจากภาษาอังกฤษ → ไทย โดยอัตโนมัติ
- ✅ รองรับข้อความที่ถูกเลือกไว้บนหน้าจอ (ไม่ต้อง Ctrl+C เอง)
- ✅ กดปุ่มลัดเพื่อแปลจากตรงที่กำลังดูอยู่ได้ทันที
- ✅ หน้าต่าง popup แบบไม่เกะกะ ซ่อนได้ ย่อได้
- ✅ ตั้งค่าปุ่มลัดเองได้ตามสะดวก
- ✅ เปิดหน้า Google Translate ได้ในคลิกเดียว

---

## 💻 วิธีติดตั้ง

1. ติดตั้ง Python 3.x หากยังไม่มี  
2. ติดตั้งไลบรารีที่จำเป็น:

```bash
pip install pyperclip pyautogui keyboard googletrans==4.0.0-rc1
