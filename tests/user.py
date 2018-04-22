"""用户测试"""
import hashlib
import unittest

from trip.service import user


class UserTestCase(unittest.TestCase):
    def test_signup(self):
        new_user = user.sign_up('hello', '123456')
        self.assertEqual('hello', new_user.name)
        self.assertEqual(hashlib.sha3_512('123456'.encode('utf-8')).hexdigest(), new_user.password_hash)


if __name__ == '__main__':
    unittest.main()
