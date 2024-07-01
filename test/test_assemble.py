import unittest
from icfp import assemble


class AssemblerTests(unittest.TestCase):
    def test_assemble_string(self) -> None:
        self.assertEqual(r'SB%,,/}Q/2,$_', assemble.assemble_token("#S{Hello World!}"))

    def test_assemble_integer(self) -> None:
        self.assertEqual('I/6', assemble.assemble_token('#I{1337}'))

    def test_assemble_var(self) -> None:
        self.assertEqual('v$', assemble.assemble_token("#v{3}"))
        self.assertEqual('L!', assemble.assemble_token("#L{0}"))

    def test_assemble_other(self) -> None:
        self.assertEqual('B$', assemble.assemble_token("B$"))

    def test_assemble_message(self) -> None:
        self.assertEqual('B- B+ I" I" I#', assemble.assemble_message("B- B+\t#I{1}   #I{1}\n#I{2}"))


if __name__ == '__main__':
    unittest.main()
