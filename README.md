# Hotspot Poll System – by Eng.Abdulmajeed

📊 مشروع استفتاء ديناميكي يُستخدم داخل صفحات تسجيل الدخول في نظام MikroTik Hotspot.

## الملفات:
- `poll.js`: ملف يحتوي على السؤال والخيارات ويُحدث من خلال البوت.
- `CUSTOM-LICENSE.md`: الرخصة المخصصة للاستخدام الشخصي فقط.

## الاستخدام:
1. فعّل GitHub Pages من إعدادات المستودع.
2. انسخ رابط `poll.js`.
3. أضف الرابط داخل login.html في الراوتر هكذا:
   ```html
   <script src="https://abdulmajeed773.github.io/samanet-poll/poll.js"></script>