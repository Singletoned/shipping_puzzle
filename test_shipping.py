# -*- coding: utf-8 -*-

import unittest

import shipping


class Port(unittest.TestCase):
    def test_init(self):
        p = shipping.Port("Flibble", "F")
        self.assertEqual(p.name, "Flibble")
        self.assertEqual(p.key, "F")
        self.assertEqual(p.routes, set())


class TestRoute(unittest.TestCase):
    def test_init(self):
        p = shipping.Port("Flibble", "F")
        r = shipping.Route(p, "bar", 5)
        self.assertEqual(r.start, p)
        self.assertEqual(r.end, "bar")
        self.assertEqual(r.days, 5)
        self.assertIn(r, p.routes)


class TestMap(unittest.TestCase):
    def test_init(self):
        m = shipping.Map()
        self.assertEqual(m.ports, set())
        self.assertEqual(m.routes, set())

    def test_add_route(self):
        m = shipping.Map()
        p = shipping.Port("Flibble", "F")
        r = shipping.Route(p, "bar", 5)
        m.add_route(r)
        self.assertEqual(m.routes, set([r]))
        self.assertEqual(m.ports, set([p, "bar"]))


if __name__ == '__main__':
    unittest.main()
