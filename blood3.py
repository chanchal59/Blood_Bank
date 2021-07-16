import sqlite3 as sql
import os
x = sql.connect("Blood__Bank.db")
c = x.cursor()
# c.execute("""create table Donate_blood(name varchar,bloodgroup varchar,
			# unit integer);""")
# c.execute("""create table purchase(name varchar,bloodgroup varchar,unit integer);""")			
while 1:
	os.system("cls")
	print("BLOOD BANK")
	print("1 Donate Blood")
	print("2 Purchase Blood")
	print("3 Admin")
	print("4 Exit")
	r = input("Choose any number::>>>")	
	if r=="1":
		os.system("cls")
		name = input("Enter your Name = ")
		bloodgroup = input("Enter your bloodgroup = ")
		unit = int(input("Enter your donate blood unit = "))
		q = ("insert into Donate_blood(name,bloodgroup,unit) values('{}','{}',{})".format(name,bloodgroup,unit))
		c.execute(q)
		x.commit()
		print("Details are successfully submitted >>...Name = '{}', Blood Group = '{}', unit = {}".format(name,bloodgroup,unit))
		input()
	elif r=="2":
		os.system("cls")
		name = input("Enter your name = ")
		bloodgroup = input("Enter your bloodgroup = ")
		bloodgroup2 = ("select bloodgroup from Donate_blood")
		c.execute(bloodgroup2)
		data4 = c.fetchall()
		for i in data4:
			if i==("{}".format(bloodgroup)):
				print("yes blood is available")
				unit = int(input("Enter your purchased blood unit = "))
				unit2 = ("select  unit from Donate_blood where bloodgroup='{}'".format(bloodgroup))
				c.execute(unit2)
				data3 = c.fetchall()
				e = 0
				for j in range(len(data3)):
					e+=int(data3[j][0])
					if e >= unit:
						q = ("insert into purchase(name,bloodgroup,unit) values('{}','{}',{})".format(name,bloodgroup,unit))
						c.execute(q)
						x.commit()
						print("Details are successfully submitted>>... Purchasor name : '{}', Bloodgroup : '{}', unit : {}".format(name,bloodgroup,unit))
						d = unit - e
						w = ("update Donate_blood set unit='{}' where bloodgroup='{}'".format(d,bloodgroup))
						c.execute(w)
						input()
			else:
				print("Blood Not Available")
				input()
	elif r=="3":
		os.system("cls")
		print("\t\t\t\t\t\tLOGIN\t\t\t\t\t\t\t")
		username = input("Username = ")
		password = input("password = ")
		if username=="chanchal" and password=="dhawan":
			print("1 Donor details\n 2 Purchasor details")
			p = input("choose any one::>>>")
			if p=="1":
				f = ("select * from Donate_blood")
				c.execute(f)
				data1 = c.fetchall()
				for i in data1:
					print("Donor name : {}, Bloodgroup : {}, Donated Blood Unit : {}".format(i[0],i[1],i[2]))
					print("------------------------------------------")
					input()
			elif p=="2":
				f = ("select * from purchase")
				c.execute(f)
				data2 = c.fetchall()
				for i in data2:
					print("Purchasor name : {}, bloodgroup : {}, Purchased Blood Unit : {}".format(i[0],i[1],i[2]))
					print("--------------------------------------------")
					input()		
		else:
			print("Invalid details")
	elif r=="4":
		print("exit")
	else:
		print("*****invalid information*****")		


