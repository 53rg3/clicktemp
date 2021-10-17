import unittest
from ccli import main
from test_helpers import run


class Hello(unittest.TestCase):

    def test_noArgs(self):
        result = run(main, ["hello"])
        assert result.exit_code == 0
        assert 'Hello, World!' in result.output

    def test_helloBob(self):
        result = run(main, ["hello", "-n", "Bob"])
        assert 'Hello, Bob!' in result.output

    def test_helloBobVerbose(self):
        result = run(main, ["--verbose", "hello", "-n", "Bob"])
        print(result.output)
        assert 'Running in mode: VERBOSE' in result.output
        assert 'Hello, Bob!' in result.output


if __name__ == '__main__':
    unittest.main()
