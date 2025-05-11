import unittest
import lla2xyz
import math
class TestLLA2XYZ(unittest.TestCase):

    def test_latitude(self):
        x, y, z = lla2xyz.compute_lla2xyz(13.021175881, 77.570397730, 842.1276)
        self.assertAlmostEqual(x, 1337933.75936599, places=4)
        self.assertAlmostEqual(y, 6070315.881011085, places=4)
        self.assertAlmostEqual(z, 1427877.5089900699, places=4)
        with self.assertRaises(ValueError):
            lla2xyz.compute_lla2xyz(math.degrees((3*(math.pi))), 0, 0)
        with self.assertRaises(TypeError):
            lla2xyz.compute_lla2xyz("10", 0, 0)

if __name__ == "__main__":
    unittest.main()