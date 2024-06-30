import unittest

from icfp import decode


class DecoderTests(unittest.TestCase):
    def test_decode_int(self) -> None:
        self.assertEqual(1337, decode.decode_int('/6'))

    def test_decode_string(self) -> None:
        self.assertEqual("Hello World!", decode.decode_string(r'B%,,/}Q/2,$_'))

    def test_decode_message(self) -> None:
        self.assertEqual("get index", decode.decode_message(r"""S'%4}).$%8"""))
        self.assertEqual("Hello World!", decode.decode_message(r"B$ B$ L# L$ v# B. SB%,,/ S}Q/2,$_ IK"))

    def test_simple_call(self) -> None:
        self.assertEqual("42", decode.decode_message("B$ L# v# IK"))

    def test_indirect_call(self) -> None:
        self.assertEqual("42", decode.decode_message("B$ B$ L# L$ v$ S- IK"))
        self.assertEqual("Hello", decode.decode_message("B$ B$ L# L$ v# SB%,,/ IK"))

    def test_nested_call(self) -> None:
        self.assertEqual("12", decode.decode_message("I-"))
        self.assertEqual("12", decode.decode_message("B+ I' I'"))
        self.assertEqual("12", decode.decode_message("B+ I' B* I$ I#"))
        self.assertEqual("12", decode.decode_message("B+ B* I$ I# B* I$ I#"))
        self.assertEqual("12", decode.decode_message(r"""B$ L" B+ v" v" B* I$ I#"""))
        self.assertEqual("12", decode.decode_message(r"""B$ L# B$ L" B+ v" v" B* I$ I# v8"""))

    def test_return_lambda(self) -> None:
        self.assertIn("function", decode.decode_message("L# I#"))
        self.assertIn("function", decode.decode_message("B$ L# L$ v# IK"))
        self.assertIn("function", decode.decode_message("B$ L# L$ v$ IK"))
        self.assertIn("function", decode.decode_message("B$ L# L$ v4 IK"))

    def test_if(self) -> None:
        self.assertEqual("no", decode.decode_message("? B> I# I$ S9%3 S./"))

    def test_mod(self) -> None:
        # Do mod in stupid unmathematical way
        self.assertEqual("-1", decode.decode_message("B% U- I( I#"))

    def test_divide(self) -> None:
        # Division needs to truncate towards zero and not floor
        self.assertEqual("3", decode.decode_message("B/ I( I#"))
        self.assertEqual("-3", decode.decode_message("B/ U- I( I#"))

    def test_multiply(self) -> None:
        self.assertEqual("6", decode.decode_message("B* I$ I#"))

    def test_int_to_string(self) -> None:
        self.assertEqual("test", decode.decode_message("U$ I4%34"))
        self.assertEqual("c", decode.decode_message("U$ B+ I\" I\""))

    def test_string_to_int(self) -> None:
        self.assertEqual("15818151", decode.decode_message("U# S4%34"))
        self.assertEqual("15818151", decode.decode_message("U# B. S4% S34"))

    def test_recursion(self) -> None:
        self.assertEqual("2", decode.decode_message('B$ L! B$ v! I" L! B+ v! v!'))
        self.assertEqual("4", decode.decode_message('B$ L! B$ v! B$ v! I" L! B+ v! v!'))

    def test_read_int(self) -> None:
        self.assertEqual("e", decode.decode_message('U$ B+ I# I#'))
        self.assertEqual("4", decode.decode_message('U$ B+ I# I#', read_int=True))
        self.assertEqual("2", decode.decode_message(r"""S#~~S/5}3#/2%$}3/-%}0/).43}&/2}53).'}4(%}%#(/}3%26)#%_~""",
                                                    read_int=True))

    def test_language_test(self) -> None:
        with open("../test_inputs/language_test.txt") as f:
            self.assertEqual("Self-check OK, send `solve language_test 4w3s0m3` to claim points for it",
                             decode.decode_message(f.read()))

    def test_efficiency1(self) -> None:
        with open("../test_inputs/efficiency1.txt") as f:
            self.assertEqual("17592186044416",
                             decode.decode_message(f.read()))


if __name__ == '__main__':
    unittest.main()
