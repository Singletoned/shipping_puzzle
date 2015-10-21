# -*- coding: utf-8 -*-

import functools


class InvalidRoute(Exception):
    pass


class Port(object):
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.routes = set()


class Route(object):
    def __init__(self, start, end, days):
        self.start = start
        self.end = end
        self.days = days
        self.start.routes.add(self)

    def __repr__(self):
        return "<Route %s-%s>" % (self.start.name, self.end.name)


@functools.total_ordering
class Path(object):
    def __init__(self):
        self.routes = []
        self.days = 0

    def __eq__(self, other):
        return self.days == other.days

    def __lt__(self, other):
        return self.days < other.days

    def add_route(self, route):
        if self.routes:
            last_route = self.routes[-1]
            if not route.start == last_route:
                raise InvalidRoute()
        self.routes.append(route)
        self.days = self.days + route.days


class Map(object):
    def __init__(self):
        self.ports = set()
        self.routes = set()

    def add_route(self, route):
        self.routes.add(route)
        self.ports.add(route.start)
        self.ports.add(route.end)
