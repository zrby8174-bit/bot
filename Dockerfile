# اختيار نسخة بايثون
FROM python:3.12-slim

# تحديد مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# أمر التشغيل
CMD ["python", "main.py"]
