Bu klasor icerisinde yer alan dosyalari forum veri tabani uzerinden export edip Json olarak sakliyorum. gitignore ile suan repository uzerinde bulunmasin diye isaretledim. Dosyalar icin bana mail atabilirsiniz (ovarol2005@gmail.com). 

Uyelerin bazi bilgileri verilerin icinde olmasi diye sadece ise yarayabilecek bir kismini kullaniyoruz.

``` sql
SELECT id_member, kulup_no, member_name, bolum, date_registered, posts, last_login, real_name, email_address, gender, total_time_logged_in, id_post_group, additional_groups FROM test.otkn_members;
```