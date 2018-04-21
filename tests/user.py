import unittest

from trip.service import user


class UserTestCase(unittest.TestCase):
    def test_create(self):
        user.signup('hello', '123456')


if __name__ == '__main__':
    unittest.main()
