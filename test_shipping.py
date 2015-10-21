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


class TestPath(unittest.TestCase):
    def test_init(self):
        path = shipping.Path()
        self.assertEqual(path.routes, [])
        self.assertEqual(path.days, 0)

    def test_add_route(self):
        path = shipping.Path()
        p = shipping.Port("Flibble", "F")
        r = shipping.Route(p, "bar", 5)
        path.add_route(r)
        self.assertEqual(path.routes, [r])
        self.assertEqual(path.days, 5)

    def test_add_route_invalid(self):
        path = shipping.Path()
        p0 = shipping.Port("Zero", "Z")
        p1 = shipping.Port("One", "O")
        p2 = shipping.Port("Two", "T")
        p3 = shipping.Port("Three", "Th")
        r0 = shipping.Route(p0, p1, 5)
        r1 = shipping.Route(p2, p3, 3)
        path.add_route(r0)
        self.assertRaises(
            shipping.InvalidRoute,
            path.add_route,
            r1)


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
