class student:

	def __init__(self,usn=None,name=None,age=None):
		self.usn=usn
		self.name=name
		self.age=age

	def getdata(self):
		self.usn=input("Enter the USN: ")
		self.name=input("Enter the name: ")
		self.age=int(input("Enter the age: "))

	def display(self):
		print("USN: ",self.usn)
		print("NAME: ",self.name)
		print("AGE: ",self.age)

class UGstudent(student):

	def __init__(self,sem=None,fee=None,stipend=None):
		self.sem=sem
		self.fee=fee
		self.stipend=stipend

	def UGgetdata(self):
		self.sem=input("Enter the semester: ")
		self.fee=int(input("Enter the fee: "))
		self.stipend=int(input("Enter the stipend: "))

	def UGdisplay(self):
		print("SEMESTER: ",self.sem)
		print("FEE: ",self.fee)
		print("STIPEND: ",self.stipend)

class PGstudent(student):

	def __init__(self,sem=None,fee=None,stipend=None):
		self.sem=sem
		self.fee=fee
		self.stipend=stipend

	def PGgetdata(self):
		self.sem=input("Enter the semester: ")
		self.fee=int(input("Enter the fee: "))
		self.stipend=int(input("Enter the stipend: "))

	def PGdisplay(self):
		print("SEMESTER: ",self.sem)
		print("FEE: ",self.fee)
		print("STIPEND: ",self.stipend)


s1=UGstudent()

s1.getdata()
s1.UGgetdata()
s1.display()
s1.UGdisplay()



s2=PGstudent()

s2.getdata()
s2.PGgetdata()
s2.display()
s2.PGdisplay()
