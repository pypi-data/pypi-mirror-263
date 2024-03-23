import unittest
import time

from vigi.utils.fps_calculator import FPSCalculator

class TestFpsCalculator(unittest.TestCase):
    def test_fps_calculator(self):
        # Test the FPS calculator
        fps_calculator = FPSCalculator(max_history_size=50)

        for i in range(100):
            fps_calculator.update()
            time.sleep(0.02)

        self.assertIn(fps_calculator.current_fps(), (42, 43, 44))

    def test_fps_calculator_no_history(self):
        # current_fps should return None if the history is not long enough
        fps_calculator = FPSCalculator(min_history_size=100)

        for i in range(50):
            fps_calculator.update()
            time.sleep(0.01)

        self.assertIsNone(fps_calculator.current_fps())
