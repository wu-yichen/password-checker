import unittest
import password_check


class TestPasswordCheck(unittest.TestCase):

    def test_get_response_from_API_without_hash_password(self):
        result = password_check.get_response_from_API('123')
        self.assertEqual(result.status_code, 400)

    def test_get_response_from_API_with_hash_password(self):
        hashed_password = '40BD0'
        result = password_check.get_response_from_API(hashed_password)
        self.assertEqual(result.status_code, 200)

    def test_hash_password(self):
        result = password_check.hash_password('123')
        result2 = password_check.hash_password('123')
        self.assertEqual(result, result2)


if __name__ == '__main__':
    unittest.main()
