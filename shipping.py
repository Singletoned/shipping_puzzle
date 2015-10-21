# -*- coding: utf-8 -*-

import functools
import heapq


class InvalidRoute(Exception):
    pass


class Port(object):
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.routes = set()

    def __repr__(self):
        return "<Port %s>" % self.name

@functools.total_ordering
class Route(object):
    def __init__(self, start, end, days):
        self.start = start
        self.end = end
        self.days = days
        self.start.routes.add(self)

    def __repr__(self):
        return "<Route %s-%s>" % (self.start.name, self.end.name)

    def __eq__(self, other):
        return self.days == other.days

    def __lt__(self, other):
        return self.days < other.days


@functools.total_ordering
class Path(object):
    def __init__(self, *args):
        self.routes = []
        self.days = 0
        for route in args:
            self.add_route(route)

    @property
    def ports(self):
        stops = [r.start for r in self.routes]
        stops.append(self.end)
        return stops

    def __eq__(self, other):
        return self.days == other.days

    def __lt__(self, other):
        return self.days < other.days

    def __repr__(self):
        return "<Path %s>" % ("-".join([p.key for p in self.ports]))

    @property
    def start(self):
        return self.routes[0].start

    @property
    def end(self):
        return self.routes[-1].end

    @classmethod
    def from_path(cls, path):
        new_path = cls()
        new_path.routes = list(path.routes)
        new_path.days = path.days
        return new_path

    def add_route(self, route):
        if self.routes:
            if not route.start == self.end:
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

    def find_path(self, start, end):
        return next(self.yield_all_paths(start, end))

    def yield_all_paths(self, start, end):
        starting_points = [
            r for r in self.routes if r.start == start]
        paths = [Path(r) for r in starting_points]
        heapq.heapify(paths)
        while paths:
            shortest = heapq.heappop(paths)
            if shortest.end == end:
                yield shortest
            else:
                for route in sorted(shortest.end.routes):
                    if route not in shortest.routes:
                        new_path = Path.from_path(shortest)
                        new_path.add_route(route)
                        heapq.heappush(paths, new_path)
