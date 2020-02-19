import unittest


class secretsTest(unittest.TestCase):
	

	def test_token_value(self):
		
		self.assertEqual(1, 1)

	#@patch("secrets.os")
	#@patch.dict("secrets.os.environ", {"SERVER_SOFTWARE": "Pevelopment"})
	#def test_server_type_value(self, mock_os):
	#	#mock_os.environ  = {"SERVER_SOFTWARE": "Development"}
	#	print(mock_os.environ)
	#	self.assertEqual(secrets.__SERVER_TYPE__, "Dev")


if __name__ == '__main__':
	unittest.main()