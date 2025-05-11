import unittest
import rotation
import numpy as np
class TestRotation(unittest.TestCase):
    
    def test_rotation(self):
        np.testing.assert_allclose( rotation.compute_RM(30), [[0.8660254, 0.5], [-0.5, 0.8660254]], rtol=1e-7)
        with self.assertRaises(TypeError):
            rotation.compute_RM("90")
        with self.assertRaises(TypeError):
            rotation.compute_RM(1 + 2j)
        with self.assertRaises(ValueError):
            rotation.compute_RM(float('nan'))
        with self.assertRaises(ValueError):
            rotation.compute_RM(float('inf'))


if __name__ == "__main__":
    unittest.main()