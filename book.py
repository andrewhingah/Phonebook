#this is a class to implement phonebook features
class Book(object):
	def __init__(self):
		self.book = {}
	def create_contact (self, name, phone_number):
		self.book[name]=phone_number
		return {"message""contact created successfully"}

	def view_contact (self, name):
		pass
	def update_contact (self, name, phone_number):
		pass
	def delete_contact (self, name):
		pass