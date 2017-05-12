from unittest import TestCase


class TestBuild(TestCase):
    #check_if_number_is_none
    #check_if_num_is_0_giveoutput_0
    #check_if_num_is_0_giveoutput_0
    #check_output

    def test_check_if_number_is_none(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build(None)
        self.assertEqual(False, result)

    def test_check_if_num_is_0_giveoutput_0(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build(0)
        self.assertEqual(0, result)

    def test_check_if_num_is_1_giveoutput_1(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build(1)
        self.assertEqual(1, result)

    def test_check_output(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build(10)
        self.assertEqual(5, result)
