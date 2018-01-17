import unittest
from crypto import mycrypto


class CryptoTest(unittest.TestCase):
    tryfilename = "test_message_encrypted_try.txt"
    correctfilename = "test_message_encrypted_correct.txt"
    message = 'hey, it works!'

    def test_encryption(self):
        mycrypto.encrypt_and_write(self.message, "testPublic.key", self.tryfilename)
        text_try = mycrypto.myfile.readfile(self.tryfilename)
        text_correct = mycrypto.myfile.readfile(self.correctfilename)
        self.assertEqual(text_try, text_correct)


def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(CryptoTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
