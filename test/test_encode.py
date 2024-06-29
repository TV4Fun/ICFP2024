import unittest

from icfp import encode


class EncoderTests(unittest.TestCase):
    def test_encode_string(self):
        self.assertEqual(encode.encode_string("Hello World!"), r"B%,,/}Q/2,$_")
        self.assertEqual(encode.encode_string("get index"), r"""'%4}).$%8""")

    def test_encode_int(self):
        self.assertEqual(encode.encode_int(1337), '/6')


if __name__ == '__main__':
    unittest.main()
