fetch("/notice.json")
  .then(res => res.json())
  .then(data => {
    alert(data.message);  // يمكن استبداله بـ modal جميل
  });
