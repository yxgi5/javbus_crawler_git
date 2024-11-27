# javbus_crawler

使用前修改 `crawler.py`的入口链接 以及 cookie

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

sqlite3数据库建立的条目有

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
无码      INTEGER)
```

可以很方便修改为传参数调用 `singleurl_handler`
