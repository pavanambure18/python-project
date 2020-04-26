import unittest
import account as AccountClass

class Test(unittest.TestCase):
    accInfo = AccountClass.account()

    def test_check_password_length(self):
        print("Checking possible Passwords\n")
        passwordList = [ 'abeautifulday', 'astrictboss', 'alovelyhouse' ]

        for password in passwordList:
            print("checking password" + password + "\n")
            passInfo = self.accInfo.check_password_length(password)
            self.assertTrue(passInfo)

if __name__ == '__main__':
    unittest.main()
