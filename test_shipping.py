# -*- coding: utf-8 -*-

import unittest

import shipping


class TestRoute(unittest.TestCase):
    def test_init(self):
        r = shipping.Route("foo", "bar", 5)
        self.assertEqual(r.start, "foo")
        self.assertEqual(r.end, "bar")
        self.assertEqual(r.days, 5)


class TestMap(unittest.TestCase):
    def test_init(self):
        m = shipping.Map()
        self.assertEqual(m.ports, set())
        self.assertEqual(m.routes, set())


if __name__ == '__main__':
    unittest.main()
