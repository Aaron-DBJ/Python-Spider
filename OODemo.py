# coding=utf-8
import imp
import sys
imp. reload(sys)


class SchoolMember:
	"""docstring for SchoolMember"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('{} is initialized'.format(self.name))

	def showInfo(self):
		print("name:{},age:{}".format(self.name, self.age))


class Student(SchoolMember):
	"""docstring for Student"""
	def __init__(self, name, age, marks):
		self.name = name
		self.age = age
		self.marks = marks
		print("student {} is initialize".format(self.name))

	def showInfo(self):
		SchoolMember.showInfo(self)
		print("Marks:{}".format(self.marks))


class Teacher(SchoolMember):
	"""docstring for Teacher"""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print("teacher {} is initialized".format(self.name))

	def showInfo(self):
		SchoolMember.showInfo(self)
		print("工资:{:d}".format(self.salary))


teacher = Teacher("Tony", 32, 6432)
student = Student("mac", 18, 98)

teacher.showInfo()
student.showInfo()
		
		
		