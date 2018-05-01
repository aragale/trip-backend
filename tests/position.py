""" Position test case """
import datetime
import json
import unittest

from trip.models import Position, as_position, as_position_list


class PositionTestCase(unittest.TestCase):
    def test_deserialize(self):
        json_string = '''
  {
    "time": "2018-04-20 23:11:11",
    "longitude": 111.11,
    "latitude": 111.11
  }'''
        positions = as_position(json_string)
        print(positions)

    def test_deserialize_list(self):
        json_string = '''[
  {
    "time": "2018-04-20 23:11:11",
    "longitude": 111.11,
    "latitude": 111.11
  },
  {
    "time": "2018-04-20 23:11:11",
    "longitude": 111.11,
    "latitude": 111.11
  }
]'''
        positions = as_position_list(json_string)
        self.assertEqual(len(positions), 2)

    def test_serialize(self):
        p = Position(time=str(datetime.datetime.now()), latitude=111.11, longitude=100.11)
        print(json.dumps(p))
