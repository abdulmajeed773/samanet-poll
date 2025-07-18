# 📢 مشروع SamaNet Alert System

نظام يتيح إرسال تنبيهات وإعلانات فورية للمستخدمين المتصلين بشبكة MikroTik  
باستخدام بوت Telegram وواجهة HTML خفيفة داخل الشبكة.

## 🔧 المميزات:
- إرسال التنبيه من Telegram في أي لحظة
- ظهور الرسالة لجميع الأجهزة المصادقة وغير المصادقة
- بدون جدولة أو انتظار
- قابل للتوسع مع رسائل خاصة حسب IP أو MAC

## 🚀 التركيب
1. تأكد من تثبيت المتطلبات:
   pip install -r backend/requirements.txt
   
2. شغّل السيرفر:
   cd backend flask run

3. أرسل رسالة من البوت إلى endpoint:


curl -X POST http://<server_ip>:5000/notify -d '{"message": "🔔 سيتم فصل الشبكة بعد قليل"}' -H "Content-Type: application/json"
