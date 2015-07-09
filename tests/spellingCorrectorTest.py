import unittest
from scdr.spellingCorrector import correct

class CorrectorTestCase(unittest.TestCase):

    def test_beutiful(self):
        """Beutiful should be corrected to beautiful."""
        self.assertEqual(correct('beutiful'), 'beautiful')

    def test_beautiful(self):
        """Beautiful is correct, it should be corrected to beautiful."""
        self.assertEqual(correct('beautiful'), 'beautiful')

if __name__ == "__main__":
    unittest.main()
