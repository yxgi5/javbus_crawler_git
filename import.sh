#!/bin/bash


#sqlite3 kkhai1.db <<EOF
sqlite3 javbus.sqlite3.db <<EOF
drop table if exists JAVBUS_DATA;
CREATE TABLE JAVBUS_DATA(
            URL       TEXT PRIMARY KEY,
            識別碼    TEXT,
            標題      TEXT,
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
            無碼      INTEGER);
.mode csv
.separator |
.header off
.import javbus.csv JAVBUS_DATA
.exit
EOF




