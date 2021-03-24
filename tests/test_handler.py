import unittest
import index


class TestHandlerCase(unittest.TestCase):
    @unittest.skip("Seeing if works on prod")
    def test_response(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
