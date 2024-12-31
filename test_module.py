

import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot(self):
        self.assertIsNotNone(draw_plot())

if __name__ == "__main__":
    unittest.main()
