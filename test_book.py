#unit tests that will ensure
#that this app is stable and runs as expected
import unittest
from book import Book

class BookTestCase (unittest.TestCase):
	def test_create_contact (self):
		boo=Book()
		response=boo.create_contact("phone_number", 72233233)
		self.assertEqual (response, {"message","contact created successfully"})
	def test_view_contact (self):
		boo=Book()
		response=boo.view_contact('john', 706088144)
		self.assertEqual (response, {'john', '706088144'})
		pass
	def test_update_contact (self):
		pass
	def test_delete_contact (self):
		pass
if __name__ == '__main__':
	unittest.main()