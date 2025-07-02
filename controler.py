#!/usr/bin/env python
#-*-coding:utf-8-*-

import sqlite3


#用来处理用Python的sqlite3操作数据库要插入的字符串中含有中文字符的时候报错处理，配合map
def _decode_utf8(aStr):
    return aStr.encode('utf-8','ignore').decode('utf-8')

def create_db():
    '''create a db and table if not exists'''
    
    # conn = sqlite3.connect("javbus.sqlite3.db")
    try:
        conn = sqlite3.connect("file:javbus.sqlite3.db?mode=rw", uri=True)

    except sqlite3.OperationalError:
        # handle missing database case
        conn = sqlite3.connect("javbus.sqlite3.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS JAVBUS_DATA(
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
                無碼      INTEGER);''')

        print("Table created successfully")
        cursor.close()
        conn.commit()
        conn.close()

    else:
        conn.close()

def write_data(dict_jav):
    '''write_data(dict_jav)'''

    # conn = sqlite3.connect("javbus.sqlite3.db")
    try:
        conn = sqlite3.connect("file:javbus.sqlite3.db?mode=rw", uri=True)
    except sqlite3.OperationalError:
        create_db()
        conn = sqlite3.connect("file:javbus.sqlite3.db?mode=rw", uri=True)
    
    cursor = conn.cursor()
    #对数据解码为unicode
    insert_data = list(map(_decode_utf8, (dict_jav['URL'], dict_jav['識別碼'], dict_jav['標題'], dict_jav['封面'], dict_jav['樣品圖像'], dict_jav['發行日期'], dict_jav['長度'], dict_jav['導演'], dict_jav['製作商'], dict_jav['發行商'], dict_jav['系列'], dict_jav['演員'], dict_jav['類別'], dict_jav['磁力链接'])))
    insert_data.append(dict_jav['無碼'])
    #插入数据
    try:
        cursor.execute('''
        INSERT INTO JAVBUS_DATA (URL, 識別碼, 標題, 封面, 樣品圖像, 發行日期, 長度, 導演, 製作商, 發行商, 系列, 演員, 類別, 磁力链接, 無碼)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', insert_data)
    except sqlite3.IntegrityError as err:
        #print(err)
        pass
    cursor.close()
    conn.commit()
    conn.close()

def refresh_data(dict_jav, url):
    '''write_data(dict_jav)'''

    # conn = sqlite3.connect("javbus.sqlite3.db")
    try:
        conn = sqlite3.connect("file:javbus.sqlite3.db?mode=rw", uri=True)
    except sqlite3.OperationalError:
        create_db()
        conn = sqlite3.connect("file:javbus.sqlite3.db?mode=rw", uri=True)
    
    cursor = conn.cursor()
    # cursor.execute('select _rowid_ from JAVBUS_DATA where URL=? COLLATE NOCASE', (url,))
    # rowid = cursor.fetchall()
    # cursor.execute('delete from JAVBUS_DATA where _rowid_=?', (rowid,))
    cursor.execute('update JAVBUS_DATA set 磁力链接=? where URL=? COLLATE NOCASE', (dict_jav['磁力链接'].encode('utf-8','ignore').decode('utf-8'), url))

    cursor.close()
    conn.commit()
    conn.close()

def check_url_not_in_table(url):
    """check_url_in_db(url),if the url isn't in the table it will return True, otherwise return False"""

    conn = sqlite3.connect("javbus.sqlite3.db")
    cursor = conn.cursor()
    # print(url)
    # cursor.execute('select URL from JAVBUS_DATA where URL=?', (url.decode('utf-8'),))
    cursor.execute('select URL from JAVBUS_DATA where URL=? COLLATE NOCASE limit 1', (url,))
    check = cursor.fetchall()
    cursor.close()
    conn.close()
    if check:
        return False
    return True

def read_magnets_from_table(url):
    """read_magnets_from_table(url),if the url isn't in the table it will return True, otherwise return False"""

    conn = sqlite3.connect("javbus.sqlite3.db")
    cursor = conn.cursor()
    # print(url)
    # cursor.execute('select URL from JAVBUS_DATA where URL=?', (url.decode('utf-8'),))
    cursor.execute('select 磁力链接 from JAVBUS_DATA where URL=? COLLATE NOCASE', (url,))
    check = cursor.fetchall()
    cursor.close()
    conn.close()
    if check:
        return check
    return