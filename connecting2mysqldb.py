import mysql.connector

cnx = mysql.connector.connect(user='root', password='77277874',host='127.0.0.1',database='school')
cursor = cnx.cursor()
cursor.execute('insert into std values (\'3333\',\'333\',\'333\',\'m\',\'2003,01,02\',\'18\')')
cnx.commit()#thats makes u sure that query has been exiquted sucsesfully *******
cnx.close()