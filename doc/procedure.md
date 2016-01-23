

#MySQL-pythonインストール手順
pythonのDB接続のためのドライバ「MySQL for python」をインストールします

##0,MySQL-pythonのバージョンを調べる
```
sudo yum list MySQL-python 
```
を実行すると、26なんとかと、27なんとかの二つのバージョンが出てくる
インストールはどっちも成功するが、pythonでimportが成功したのは27の方でした。

##1,yumでインストール
```CentOS
sudo yum install MySQL-python-27なんとか
```
を実行すると自動でインストール。一分はかからない

##2,pythonで確かめる
インストールのあと特に作業はいりません。
pythonを起動して、

```python:python
import MySQLdb
```
を実行し、エラーがかえってこなければ成功です。