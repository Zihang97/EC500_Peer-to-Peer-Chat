import pymysql
import time

password = "150417jzh"
db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
cursor = db.cursor()

def create_user(cursor, name, ip):
	sql = "insert into user (name, ip) values(%s, %s)"
	cursor.execute(sql, (name, ip))

	db.commit()


def get_ip(cursor, name):
	sql = "select * from user where name = %s"
	cursor.execute(sql, (name))

	result = cursor.fetchone()

	ip = result[1]
	return ip


def msg_to_send(cursor, name, message):
	sql = "insert into sender (ip, name, message, status, time) values(%s, %s, %s, %s, %s)"
	ip = get_ip(cursor, name)

	current_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) 
	cursor.execute(sql, (ip, name, message, 'pending', current_time))

	db.commit()

def msg_sending(cursor):
	sql = "select * from sender where status = 'pending'"
	cursor.execute(sql)

	results = cursor.fetchall()
	
	out = []

	for row in results:
		out.append(row[2])
		sql = "update sender set status = 'sent' where name = %s and message = %s"
		cursor.execute(sql, (row[1], row[2]))

	db.commit()

	return out

def msg_received(cursor, name, message):
	sql = "insert into receiver (ip, name, message, status, time) values(%s, %s, %s, %s, %s)"
	ip = get_ip(cursor, name)

	current_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) 
	cursor.execute(sql, (ip, name, message, 'received', current_time))

	db.commit()



	

	
