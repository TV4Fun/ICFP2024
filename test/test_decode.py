import unittest

from icfp import decode


class DecoderTests(unittest.TestCase):
    def test_decode_int(self):
        self.assertEqual(1337, decode.decode_int('/6'))

    def test_decode_string(self):
        self.assertEqual("Hello World!", decode.decode_string(r'B%,,/}Q/2,$_'))

    def test_decode_message(self):
        self.assertEqual("get index", decode.decode_message(r"""S'%4}).$%8"""))
        self.assertEqual("Hello World!", decode.decode_message(r"B$ B$ L# L$ v# B. SB%,,/ S}Q/2,$_ IK"))

    def test_simple_call(self):
        self.assertEqual("42", decode.decode_message("B$ L# v# IK"))

    def test_indirect_call(self):
        self.assertEqual("42", decode.decode_message("B$ B$ L# L$ v$ S- IK"))
        self.assertEqual("42", decode.decode_message("B$ B$ L# L$ v# S- IK"))

    def test_nested_call(self):
        self.assertEqual("12", decode.decode_message("I-"))
        self.assertEqual("12", decode.decode_message("B+ I' I'"))
        self.assertEqual("12", decode.decode_message("B+ I' B* I$ I#"))
        self.assertEqual("12", decode.decode_message("B+ B* I$ I# B* I$ I#"))
        self.assertEqual("12", decode.decode_message(r"""B$ L" B+ v" v" B* I$ I#"""))
        self.assertEqual("12", decode.decode_message(r"""B$ L# B$ L" B+ v" v" B* I$ I# v8"""))

    def test_return_lambda(self):
        self.assertIn("function", decode.decode_message("L# I#"))
        self.assertIn("function", decode.decode_message("B$ L# L$ v# IK"))
        self.assertIn("function", decode.decode_message("B$ L# L$ v$ IK"))
        self.assertIn("function", decode.decode_message("B$ L# L$ v4 IK"))


if __name__ == '__main__':
    unittest.main()
