USERNAME = "Aniket"
PASSWORD = "Aniket1@34"

def login(username,password):
    if username == USERNAME and password == PASSWORD:
        return "Logged In".upper()

    elif len(username) == 0 and len(password) == 0:
        return "Empty credentials".upper()
    else:
        return "Invalid credentials".upper()

# print(login("",""))

import unittest
class LoginTest(unittest.TestCase):
    def test_login_with_valid_credentials(self):
        output = login("Aniket", "Aniket1@34")
        self.assertEqual(output,"Logged In".upper())
        

    def test_login_with_empty_credentials(self):
       output = login("", "")
       self.assertEqual(output,"Empty credentials".upper())
        

    def test_login_with_invalid_credentials(self):
        output = login("Aniket", "aniket1234")
        self.assertEqual(output,"Invalid credentials".upper())
        
if __name__ == '__main__':
    unittest.main()


