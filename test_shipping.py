# -*- coding: utf-8 -*-

import unittest

import shipping


class TestRoute(unittest.TestCase):
    def test_init(self):
        r = shipping.Route("foo", "bar", 5)
        assert r.start == "foo"
        assert r.end == "bar"
        assert r.days == 5


if __name__ == '__main__':
    unittest.main()
