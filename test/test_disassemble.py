import unittest

from icfp import disassemble


class DisassemblerTests(unittest.TestCase):
    def test_disassemble_string(self) -> None:
        self.assertEqual("#S{Hello World!}", disassemble.disassemble_token(r'SB%,,/}Q/2,$_'))

    def test_disassemble_integer(self) -> None:
        self.assertEqual('#I{1337}', disassemble.disassemble_token('I/6'))

    def test_disassemble_var(self) -> None:
        self.assertEqual("#v{3}", disassemble.disassemble_token('v$'))
        self.assertEqual("#L{0}", disassemble.disassemble_token('L!'))

    def test_disassemble_other(self) -> None:
        self.assertEqual("B$", disassemble.disassemble_token('B$'))


if __name__ == '__main__':
    unittest.main()
