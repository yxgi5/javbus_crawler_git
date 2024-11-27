# sqlite3数据库建立的条目有

```
URL       TEXT PRIMARY KEY,
識別碼    TEXT,
標題     TEXT,
封面      TEXT,
樣品圖像  TEXT, 
發行日期  TEXT,
長度      TEXT,
導演      TEXT,
製作商    TEXT,
發行商    TEXT,
系列      TEXT,
演員      TEXT,
類別      TEXT,
磁力链接  TEXT,
無碼      INTEGER)
```


# javbus_crawler

默認增量更新

我這裏只放了我自己的cookie，從瀏覽器調試界面獲取。

如果要修改 `crawler.py`的入口链接看下面 

`homeurl_handler`的参数可以是

```
https://www.javbus.com/ja/SDJS-270
https://www.javbus.com/ja
https://www.javbus.com/SDJS-270
https://www.javbus.com
```

`singleurl_handler`的参数可以是

```
https://www.javbus.com/ja/SDJS-270
https://www.javbus.com/SDJS-270
```


# crawler_with_param.py

通過 `auto_start.sh` 傳遞參數，每個參數實際上是list文件的一行


# all_bango

```
#!/bin/bash

sqlite3 javbus.sqlite3.db <<EOF
.header off
.out db_bango.list
select URL from JAVBUS_DATA;
.exit
EOF

cat db_bango.list | sed 's/https:\/\/www.javbus.com\/ja\///' | sed 's/https:\/\/www.javbus.com\///' | sed 's/[a-z]/\U&/g' | sort -u > db_bango.list.new
mv db_bango.list{.new,}
```

```
cat av.list | sed 's/[a-z]/\U&/g' | sort -u > av.list.new
mv av.list{.new,}

diff -y -W 100 av.list db_bango.list | grep -a -F '<' | sed 's/^\(.*\)\ .*$/\1/' | sed 's/[[:space:]][[:space:]]*//g' | sed 's/[a-z]/\U&/g' | sort -u > tmp.list

diff -y -W 100 av.list db_bango.list | grep -a -F -e '|' > diff.txt
cat diff.txt | sed -e 's/|/\n/' | sed 's/[[:space:]][[:space:]]*//g' | sed 's/[a-z]/\U&/g' | sort -u > diff.txt.new
mv diff.txt{.new,}
cat diff.txt | sed 's/[a-z]/\U&/g' | sort -u >> tmp.list
rm diff.txt

./auto_start.sh

diff -y -W 100 db_bango.list av.list | grep -a -F '<' | sed 's/^\(.*\)\ .*$/\1/' | sed 's/[[:space:]][[:space:]]*//g' | sed 's/[a-z]/\U&/g' | sort -u > input.list
mv input.list ../New
```

# download sample image

like follows, dosen't need cookie

if need proxy and referer
```
aria2c --header 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' --header 'sec-ch-ua-mobile: ?0' --header 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' --header 'sec-ch-ua-platform: "Linux"' --header 'Referer: https://www.javbus.com/ja/' --all-proxy="http://127.0.0.1:8118" \
https://www.javbus.com/imgs/bigsample/16qx_b_4.jpg
```

if dosen't need proxy nor referer
```
aria2c --header 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' --header 'sec-ch-ua-mobile: ?0' --header 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' --header 'sec-ch-ua-platform: "Linux"' \
https://pics.dmm.co.jp/digital/video/h_1416ad00524/h_1416ad00524jp-3.jpg

```

