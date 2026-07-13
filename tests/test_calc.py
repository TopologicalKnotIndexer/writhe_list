import unittest

from data.calc import generate_writhe_records, parse_pd_record


class FakeKnot:
    def __init__(self, pd_code):
        self.pd_code = pd_code

    def writhe(self):
        return len(self.pd_code)


class WritheGeneratorTests(unittest.TestCase):
    def test_safe_record_parser(self):
        self.assertEqual(parse_pd_record("[K0a1|[]]"), ("K0a1", []))
        with self.assertRaises((ValueError, SyntaxError)):
            parse_pd_record("[K0a1|__import__('os').getcwd()]")

    def test_committed_baseline_generates_all_records(self):
        output = generate_writhe_records(FakeKnot)
        lines = output.splitlines()
        self.assertEqual(len(lines), 1783)
        self.assertEqual(lines[0], "[0|[]|K0a1]")


if __name__ == "__main__":
    unittest.main()
