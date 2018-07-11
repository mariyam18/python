
import pymysql
connection = pymysql.connect('localhost','root','root','student')
cursor=connection.cursor()


def menu():
	user1="admin"
	pass1="admin"
	user2=input("ENTER THE USERNAME:")
	pass2=input("ENTER THE PASSWORD:")
	if(user2 == user1 and pass2 == pass1):
		print("-----------!!!!!!WELCOME-ACCESS GRANTED!!!!!!----------")
		while(1):
			c=int(input("""
				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: """))
			if(c is 1):
				add_detail()
			elif(c is 2):
				delete()
			elif(c is 3):
				search() 
			elif(c is 4):
				return
			else:
				print("please enter valid number")
				menu()
	else:
			print("Sorry can't access")
	
def add_detail():
	name=input("ENTER THE NAME: ")
	gender=input("F OR M: ")
	age=input("ENTER YOUR AGE: ")
	clas=input("ENTER YOUR CLASS: ")
	mob_no=input("ENTER THE MOBILE NUMBER: ")
	marks=input("ENTER YOUR MARKS: ")
	email_no=input("ENTER YOUR EMAIL: ")
	sql = "INSERT INTO detail (NAME,GENDER,AGE,CLASS,MOB_no,MARKS,EMAIL_NO) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	cursor.execute(sql,(name, gender, age, clas, mob_no, marks, email_no))
	connection.commit()
	cursor.execute("select * from detail")
	data= cursor.fetchall()
	print(data)
	
def search():
	name_s=input("ENTER THE NAME YOU WANT TO SEARCH : ")
	cursor.execute("select * from detail where NAME=%s",(name_s))
	data =cursor.fetchone()
	if(data == None):
		print('Sorry, Name not found')
	else:
		print("Id :",data[0])
		print("Name : ",data[1])
		print("Gender :",data[2])
		print("Class :",data[3])
		print("Age :",data[4])
		print("Mob_no :",data[5])
		print("Marks :",data[6])
		print("Email :",data[7])
		
def delete():
	name_d=input("ENTER THE NAME YOU WANT TO Delete : ")
	cursor.execute("delete from detail where NAME=%s",(name_d))
	connection.commit()
	print('Sucessfully deleted')
	
	
	
	
menu()	




"""
OUTPUT:

ENTER THE USERNAME:admin
ENTER THE PASSWORD:admin
-----------!!!!!!WELCOME-ACCESS GRANTED!!!!!!----------

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 1
ENTER THE NAME: ilaf
F OR M: f
ENTER YOUR AGE: 20
ENTER YOUR CLASS: 2
ENTER THE MOBILE NUMBER: 65241389
ENTER YOUR MARKS: 70
ENTER YOUR EMAIL: ilaf@gmail.com        
((1, 'muskan', 'f', '2', '19', '123346', '90', None), (2, 'heena', 'f', '2', '19', '123346', '50', None), (3, 'mariyam', 'f', '2', '19', '5876', '20', 'hgk'), (4, 'ilaf', 'f', '2', '20', '65241389', '70', 'ilaf@gmail.com'))

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 2
ENTER THE NAME YOU WANT TO Delete : muskan
Sucessfully deleted

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 3
ENTER THE NAME YOU WANT TO SEARCH : muskan
Sorry, Name not found

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 2
ENTER THE NAME YOU WANT TO Delete : heena
Sucessfully deleted

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 3
ENTER THE NAME YOU WANT TO SEARCH : mariyam
Id : 3
Name :  mariyam
Gender : f
Class : 2
Age : 19
Mob_no : 5876
Marks : 20
Email : hgk

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 3
ENTER THE NAME YOU WANT TO SEARCH : ilaf
Id : 4
Name :  ilaf
Gender : f
Class : 2
Age : 20
Mob_no : 65241389
Marks : 70
Email : ilaf@gmail.com

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 1
ENTER THE NAME: muskan
F OR M: f
ENTER YOUR AGE: 19
ENTER YOUR CLASS: 2
ENTER THE MOBILE NUMBER: 9876532
ENTER YOUR MARKS: 80
ENTER YOUR EMAIL: muskan@gmail.com
((3, 'mariyam', 'f', '2', '19', '5876', '20', 'hgk'), (4, 'ilaf', 'f', '2', '20', '65241389', '70', 'ilaf@gmail.com'), (5, 'muskan', 'f', '2', '19', '9876532', '80', 'muskan@gmail.com'))

				1:ENTER THE STUDENT DETAILS
				2:DELETE DETAIL
				3:SEARCH DETAIL 
				4:EXIT
				
				PLEASE ENTER YOUR CHOICE: 4
mariyam@mariyam:~/project$ python3 pro.py
ENTER THE USERNAME:mariyam
ENTER THE PASSWORD:mariyam
Sorry can't access


"""
