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



