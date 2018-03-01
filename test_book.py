#unit tests that will ensure
#that this app is stable and runs as expected
import unittest
from book import Book

class BookTestCase (unittest.TestCase):
	def test_create_contact (self, phone_number):
		book=Book()
		response=book.create_contact (phone_number)
		self.assertEqual (response, {"message","contact created successfully"})
	def test_view_contact (self, name):
		
		self.assertEqual (response, {"message","contact created successfully"})
		pass
	def test_update_contact (self, name, phone_number):
		pass
	def test_delete_contact (self, name):
		pass