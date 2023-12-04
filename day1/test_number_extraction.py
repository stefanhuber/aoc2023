import unittest
from day1.main import extract_number

test_cases = [
    ['threethree57', 37],
    ['five8threetprlzmrx418kdlzddbpv', 58],
    ['three7hqsnvrxhv68five1three7', 37],
    ['2sixcj651three', 23],
    ['cvfqbfftpk3six6vdvx6eightxqsjqph3', 33],
    ['914', 94],
    ['2zq9', 29],
    ['fourshjqd1six', 46],
    ['sixceight7', 67],
    ['plxhflcmqsgjpnfivemhsphvv', 55],
    ['three5ninehntgrlchcnnmqx98two5', 35],
    ['8sixcbqlfmcq14vnlmsixlhzrq', 86],
    ['4eight2dsdnpnsx', 42],
    ['fivexntprmkhpronejbnbseighttfnzmkdn3six', 56],
    ['ninejtrqtneight6rvtnqspmkjsix', 96],
    ['eightjzqzhrllg1oneightfck', 88] # overlapping
]

class TestNumberExtraction(unittest.TestCase):

    def test_should_satisfy_all_test_cases(self):
        for test_case in test_cases:
            self.assertEqual(extract_number(test_case[0]), test_case[1])
