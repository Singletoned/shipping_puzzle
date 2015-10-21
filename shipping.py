# -*- coding: utf-8 -*-


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


class Path(object):
    def __init__(self):
        self.routes = []
        self.days = 0

    def add_route(self, route):
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
