import unittest

from machinetranslation.translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_english_to_french_not_equal(self):
        self.assertNotEqual(english_to_french("Hello"), "bad translation")

    def test_french_to_english_not_equal(self):
        self.assertNotEqual(french_to_english("Bonjour"), "bad translation")

    def test_english_to_french_raise_exception(self):
        self.assertEqual(english_to_french(""), "Error occured during calling the API.")

    def test_french_to_english_raise_exception(self):
        self.assertEqual(french_to_english(""), "Error occured during calling the API.")


if __name__ == "__main__":
    unittest.main()
