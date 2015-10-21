# -*- coding: utf-8 -*-


class Route(object):
    def __init__(self, start, end, days):
        self.start = start
        self.end = end
        self.days = days

    def __repr__(self):
        return "<Route %s-%s>" % (self.start.name, self.end.name)


class Map(object):
    def __init__(self):
        self.ports = set()
        self.routes = set()

    def add_route(self, route):
        self.routes.add(route)
        self.ports.add(route.start)
        self.ports.add(route.end)
