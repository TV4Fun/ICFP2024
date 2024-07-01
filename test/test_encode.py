import unittest

from icfp import encode


class EncoderTests(unittest.TestCase):
    def test_encode_string(self) -> None:
        self.assertEqual(encode.encode_string("Hello World!"), r"B%,,/}Q/2,$_")
        self.assertEqual(encode.encode_string("get index"), r"""'%4}).$%8""")

    def test_encode_int(self) -> None:
        self.assertEqual(encode.encode_int(1337), '/6')

    def test_encode_zero(self):
        self.assertEqual('!', encode.encode_int(0))

    def test_encode_negative(self):
        with self.assertRaises(ValueError):
            encode.encode_int(-1)

    def test_encode_message(self):
        self.assertEqual(r"""B. S%#(/} U$ B- B+ I" I" I#""", encode.encode_message("echo {U$ B- B+\t#I{1}   #I{1}\n#I{2} }"))

    def test_embedded_expression(self):
        self.assertEqual("B. S%#(/} S%#(/}", encode.encode_message("echo {S%#(/} }"))


if __name__ == '__main__':
    unittest.main()
