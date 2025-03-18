
# 一般运行
比如我这里是
```
$ python3.8 crawler.py
```
只有能访问到javbus网站(且对方允许访问并且网页排版没有变动)，就会产生sqlite3格式的db文件，或者更新db文件

pip list 在本文最末尾

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


# pip list
关于 python 环境，我这里的 pip list 是
```
$ pip3.8 list
Package                       Version
----------------------------- -----------------
annotated-types               0.6.0
apt-xapian-index              0.47
apturl                        0.5.2
asn1crypto                    0.24.0
astroid                       1.6.0
async-timeout                 3.0.1
attrs                         23.2.0
Automat                       22.10.0
beautifulsoup4                4.12.2
blinker                       1.4
bottle                        0.12.13
Brlapi                        0.6.6
cachetools                    5.3.2
certifi                       2024.7.4
cffi                          1.16.0
chardet                       4.0.0
click                         8.1.7
colorama                      0.3.7
command-not-found             0.3
constantly                    23.10.4
cppman                        0.4.8
cryptography                  42.0.8
cssselect                     1.2.0
cupshelpers                   1.0
cycler                        0.10.0
Cython                        0.26.1
decorator                     4.1.2
defer                         1.0.6
defusedxml                    0.7.1
devscripts                    2.20.2-18.04.sav0
distro                        1.3.0
distro-info                   1.0+18.04sav1
docker                        2.5.1
docker-pycreds                0.2.1
docutils                      0.14
exceptiongroup                1.2.1
feedparser                    5.2.1
feeluown                      3.8.4
filelock                      3.15.4
Flask                         0.12.2
fuo-dl                        0.3
fuo-kuwo                      0.1.6
fuo-local                     0.3
fuo-netease                   0.9.2
fuo-qqmusic                   0.5.1
fuo-xiami                     0.2.4
fuo-ytmusic                   0.1.1
fuzzywuzzy                    0.18.0
galternatives                 0.92.2
gitdb2                        2.0.3
GitPython                     2.1.8
Glances                       2.11.1
gobject                       0.1.0
gpg                           1.10.0
greenlet                      0.4.12
gst                           0.1.0
h11                           0.14.0
h5py                          2.7.1
html5lib                      0.999999999
httplib2                      0.20.2
hyperlink                     21.0.0
icdiff                        1.9.1
idna                          2.10
imageio                       2.9.0
imageio-ffmpeg                0.4.4
importlib-metadata            4.6.0
importlib-resources           5.2.2
incremental                   22.10.0
influxdb                      4.1.1
ipython_genutils              0.2.0
isort                         4.3.4
itemadapter                   0.9.0
itemloaders                   1.3.1
itsdangerous                  0.24
janus                         0.6.1
jmespath                      1.0.1
kazam                         1.4.5
keyring                       10.6.0
keyrings.alt                  3.0
language-selector             0.1
lazr.restfulclient            0.14.2
lazy-object-proxy             1.3.1
leveldb                       0.1
libscrc                       1.7.1
lml                           0.1.0
logilab-common                1.4.1
louis                         3.5.0
lxml                          5.1.0
macaroonbakery                1.1.3
Mako                          1.0.7
Markdown                      2.6.9
Markups                       2.0.1
marshmallow                   3.13.0
mate-tweak                    18.4.16
matplotlib                    2.1.1
mccabe                        0.6.1
meld                          3.18.0
meson                         0.61.2
MouseInfo                     0.1.3
msgpack                       0.5.6
multidict                     6.0.4
mutagen                       1.45.1
neovim                        0.2.0
netifaces                     0.10.4
networkx                      1.11
nose                          1.3.7
numexpr                       2.6.4
numpy                         1.21.2
oauth                         1.0.1
olefile                       0.45.1
onboard                       1.4.1
opencv-contrib-python         4.5.4.58
outcome                       1.3.0.post0
packaging                     21.0
pandas                        1.3.4
parsel                        1.9.1
pexpect                       4.2.1
pickleshare                   0.7.4
Pillow                        8.3.2
pip                           24.1.2
ply                           3.11
prettytable                   3.9.0
Protego                       0.3.1
psutil                        5.4.2
pulsemixer                    1.4.0
py3dns                        3.1.1
pyasn1                        0.6.0
pyasn1_modules                0.4.0
PyAudio                       0.2.11
PyAutoGUI                     0.9.53
pycairo                       1.16.2
PyChromecast                  0.8.1
pycparser                     2.22
pycrypto                      2.6.1
pycryptodome                  3.10.1
pycryptodomex                 3.4.7
pycups                        1.9.73
pycurl                        7.43.0.1
pydantic                      1.9.2
pydantic_core                 2.14.5
PyDispatcher                  2.0.7
pyenchant                     2.0.0
pyexcel-io                    0.6.4
pyexcel-xls                   0.6.2
PyGetWindow                   0.0.9
PyGObject                     3.26.1
pyinotify                     0.9.6
PyJWT                         1.5.3
pylint                        1.8.3
pymacaroons                   0.13.0
PyMsgBox                      1.0.7
pymusic-dl                    3.0.1
PyMySQL                       1.1.1
PyNaCl                        1.1.2
PyOpenGL                      3.1.5
pyOpenSSL                     24.1.0
pyparsing                     2.4.7
pyperclip                     1.9.0
PyQt5                         5.15.9
pyqt5-plugins                 5.15.9.2.3
PyQt5-Qt5                     5.15.2
PyQt5-sip                     12.13.0
PyQt5-stubs                   5.15.6.0
pyqt5-tools                   5.15.9.3.3
PyQtWebEngine                 5.15.2
PyQtWebEngine-Qt5             5.15.2
PyRect                        0.2.0
pyRFC3339                     1.0
PyScreeze                     0.1.26
PySimpleSOAP                  1.16.2
pysmi                         0.2.2
pysnmp                        4.4.3
PySocks                       1.7.1
pystache                      0.5.4
python-apt                    1.6.6
python-dateutil               2.8.1
python-debian                 0.1.32
python-debianbts              2.7.2
python-dotenv                 1.0.0
python-gflags                 1.5.1
python-magic                  0.4.16
python-xlib                   0.20
python3-xlib                  0.15
pyttsx3                       2.90
pytube                        15.0.0
pytweening                    1.2.0
pytz                          2021.1
PyWavelets                    0.5.1
pyxattr                       0.6.0
pyxdg                         0.25
PyYAML                        3.12
qasync                        0.22.0
qt5-applications              5.15.2.2.3
qt5-tools                     5.15.2.1.3
queuelib                      1.7.0
reportbug                     7.1.8ubuntu1
reportlab                     3.4.0
requests                      2.25.1
requests-file                 2.1.0
requests-unixsocket           0.1.5
roman                         2.0.0
scikit-image                  0.13.1
scikit-video                  1.1.11
scipy                         1.10.1
scour                         0.38.2
Scrapy                        2.11.2
scrapy-splash                 0.9.0
scrapyd                       1.4.3
scrapyd-client                1.2.3
screen-resolution-extra       0.0.0
selenium                      4.23.0
service-identity              24.1.0
setproctitle                  1.1.10
setuptools                    39.0.1
simplegeneric                 0.8.1
simplejson                    3.13.2
six                           1.16.0
smmap2                        2.0.3
sniffio                       1.3.1
sortedcontainers              2.4.0
soupsieve                     2.4.1
ssh-import-id                 5.7
system-service                0.3
systemd-python                234
tables                        3.4.2
textile                       3.0.0
tkVideo                       0.1
tldextract                    5.1.2
tomlkit                       0.7.0
traitlets                     4.3.2
trio                          0.26.0
trio-websocket                0.11.1
Twisted                       24.3.0
typing_extensions             4.9.0
uberegg                       0.1.1
ubuntu-advantage-tools        8001
ubuntu-dev-tools              0.175-18.04.3
ubuntu-drivers-common         0.0.0
ufw                           0.36
unattended-upgrades           0.1
unidiff                       0.5.4
unity-scope-calculator        0.1
unity-scope-chromiumbookmarks 0.1
unity-scope-colourlovers      0.1
unity-scope-devhelp           0.1
unity-scope-firefoxbookmarks  0.1
unity-scope-manpages          0.1
unity-scope-openclipart       0.1
unity-scope-texdoc            0.1
unity-scope-tomboy            0.1
unity-scope-virtualbox        0.1
unity-scope-yelp              0.1
unity-scope-zotero            0.1
unity-tweak-tool              0.0.7
urllib3                       1.26.7
usb-creator                   0.3.3
vunit-hdl                     4.4.0
w3lib                         2.2.1
wcwidth                       0.2.12
webdriver-manager             4.0.1
webencodings                  0.5
websocket-client              1.8.0
Werkzeug                      0.14.1
wheel                         0.30.0
wrapt                         1.9.0
wsproto                       1.2.0
wxPython                      4.0.1
xdot                          0.9
xkit                          0.0.0
xlrd                          1.2.0
xlwt                          1.3.0
yarl                          1.9.2
youtube_dl                    2018.3.14
ytmusicapi                    1.3.2
zeroconf                      0.19.1
zipp                          3.17.0
zope.interface                6.4.post2

```


