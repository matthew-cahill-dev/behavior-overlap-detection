import unittest
import utils  # or main, but usually these helpers live in utils.py

class TestBehaviorChecker(unittest.TestCase):

    def setUp(self):
        # Matches your real data shape
        self.behaviors = [
            {"id": "b1", "description": "Say hello to the customer."},
            {"id": "b2", "description": "Say hello to the customer."},
            {"id": "b3", "description": "Never argue with the customer."},
            {"id": "b4", "description": "Never argue with a customer."},
        ]

    def test_find_exact_duplicates(self):
        duplicates = utils.find_exact_duplicates(self.behaviors)
        self.assertTrue(any(
            pair[0]['id'] == 'b1' and pair[1]['id'] == 'b2'
            for pair in duplicates
        ))

    def test_find_similar_behaviors(self):
        overlaps = utils.find_similar_behaviors(self.behaviors, threshold=0.90)
        self.assertTrue(any(
            pair[0]['id'] == 'b3' and pair[1]['id'] == 'b4'
            for pair in overlaps
        ))

if __name__ == '__main__':
    unittest.main()
