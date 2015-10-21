# -*- coding: utf-8 -*-

import shipping
import data


def shortest_routes():
    print "Shortest BA-L",
    print data.shipping_map.find_path(
        data.BUENOS_AIRES, data.LIVERPOOL)
    print "Shortest NY-NY",
    print data.shipping_map.find_path(
        data.NEW_YORK, data.NEW_YORK)

def number_of_routes():
    print "Number of routes from Liverpool-Liverpool"
    print data.shipping_map.find_paths_max_stops(
        data.LIVERPOOL, data.LIVERPOOL, 4)

if __name__ == '__main__':
    shortest_routes()
    number_of_routes()
