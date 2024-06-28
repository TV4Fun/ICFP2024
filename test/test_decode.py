import unittest
from icfp import decode


class DecoderTests(unittest.TestCase):
    def test_decode_int(self):
        self.assertEqual(decode.decode_int('/6'), 1337)

    def test_decode_string(self):
        self.assertEqual(decode.decode_string(r'B%,,/}Q/2,$_'), "Hello World!")

    def test_decode_message(self):
        self.assertEqual(decode.decode_message(r"""S'%4}).$%8"""), "get index")


if __name__ == '__main__':
    unittest.main()
