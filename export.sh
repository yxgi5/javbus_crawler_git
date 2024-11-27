#!/bin/bash

sqlite3 javbus.sqlite3.db <<EOF
.mode csv
.header off
.separator |
.out javbus.csv
select * from JAVBUS_DATA;
.exit
EOF



