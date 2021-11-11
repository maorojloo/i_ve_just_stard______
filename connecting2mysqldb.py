import mysql.connector

cnx = mysql.connector.connect(
user='sql5450111',
password='ZB4dedpLbP'
,host='sql5.freemysqlhosting.net'
,database='sql5450111')
cursor = cnx.cursor()
#cursor.execute('insert into std VALUES (\'bb222b\', \'bb222b\', \'bb2222b\', \'222\')')
cursor.execute('select * from std ; ')
for (a,b,c,d) in cursor:
    print(a,' | ',b,' | ',c,' | ',d,' | ')
#cnx.commit()#thats makes u sure that query has been exiquted sucsesfully *******
cnx.close()