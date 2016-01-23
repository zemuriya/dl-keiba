# -*- coding: utf-8 -*-

import MySQLdb
 
main():
	connector = MySQLdb.connect(host="localhost", db="keibadb", user="keiba",
	 passwd="", charset="utf8")
	cursor = connector.cursor()


if __name__ == "__main__":main()