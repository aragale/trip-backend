import unittest

from trip.service import session


class UserTestCase(unittest.TestCase):
    def test_sign_in(self):
        new_session = session.sign_in('hello', '123456')
        self.assertIsNotNone(new_session)

    def test_exists_by_user_name(self):
        exists = session.exists_by_user_name('hello')
        self.assertTrue(exists)

    def test_get_user_id_by_id(self):
        user = session.get_user_id_by_id('e2cc4180-be80-4d4e-aebe-21920c06cf46')
        self.assertIsNotNone(user)

    def test_sign_out(self):
        ret = session.sign_out('e2cc4180-be80-4d4e-aebe-21920c06cf46')
        self.assertEqual(ret, 1)
