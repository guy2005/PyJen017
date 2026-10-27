# PyJen017

โครงงานเดี่ยว Python CI/CD ด้วย Jenkins
- **รหัสนักศึกษา**: 6752410017
- **ชื่อโฟลเดอร์/โปรเจค**: PyJen017

---

## รายละเอียดโปรเจค
1. **calculator.py**: ฟังก์ชัน `add(a, b)` สำหรับบวกเลข
2. **main.py**: โปรแกรมรันการบวกเลขแสดงผลลัพธ์
3. **test_app.py**: Automated Unit Tests สำหรับทดสอบฟังก์ชันบวกเลขและการรันโปรแกรม
4. **Jenkinsfile**: Automated CI/CD Pipeline (Build, Lint, Test, Archive, Deploy)

---

## ขั้นตอน CI/CD Pipeline ใน Jenkins
- **Checkout**: ดึง Source Code จาก GitHub (`main` branch)
- **Setup Python**: สร้าง Virtual Environment (`venv`) และติดตั้ง Dependencies (`requirements.txt`)
- **Lint**: ตรวจสอบมาตรฐานโค้ดด้วย `flake8`
- **Test**: รัน Unit Tests ด้วย `pytest` พร้อมออกรายงานผล JUnit XML (`reports/results.xml`)
- **Build**: บีบอัดไฟล์โปรเจคเป็น `.zip` เก็บไว้ในโฟลเดอร์ `dist/` และทำ Artifact Archiving ใน Jenkins
- **Deploy**: สำเนาไฟล์โค้ดไปยังโฟลเดอร์ Deploy (`C:\Jenkins\PyJen017\deploy`) และทดลองรันโปรแกรมอัตโนมัติ
