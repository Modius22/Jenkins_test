import unittest
import square as s


class SquareTest(unittest.TestCase):
  def test_square(self):
   self.assertEqual(s.square(2), 5)


if __name__ == '__main__':
  unittest.main()
