import unittest
from crypto import mycrypto


class CryptoTest(unittest.TestCase):
    tryfilename = "test_message_encrypted_try.txt"
    correctfilename = "test_message_encrypted_correct.txt"
    message = 'hey, it works!'

    def test_decryption(self):
        text_try = mycrypto.decryption_and_return(self.correctfilename, "testPrivate.key")
        text_correct = self.message
        self.assertEqual(text_try, text_correct)


def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(CryptoTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
