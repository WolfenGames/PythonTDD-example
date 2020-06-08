import unittest

class FirstTestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('i am a test'.upper(), 'I AM A TEST')

if __name__ == '__main__':
  unittest.main()