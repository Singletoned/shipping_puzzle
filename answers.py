# -*- coding: utf-8 -*-

import shipping
import data

def exact_routes():
    print "Exact BA-NY_L",
    print data.shipping_map.find_exact_path(
        data.BUENOS_AIRES, data.NEW_YORK, data.LIVERPOOL)

    print "Exact BA-C-L",
    print data.shipping_map.find_exact_path(
        data.BUENOS_AIRES, data.CASABLANCA, data.LIVERPOOL)

    print "Exact BA-CT-NY-L-C",
    print data.shipping_map.find_exact_path(
        data.BUENOS_AIRES,
        data.CAPE_TOWN,
        data.NEW_YORK,
        data.LIVERPOOL,
        data.CASABLANCA)

    print "Exact BA-CT-C",
    print data.shipping_map.find_exact_path(
        data.BUENOS_AIRES,
        data.CAPE_TOWN,
        data.CASABLANCA)

def shortest_routes():
    print "Shortest BA-L",
    print data.shipping_map.find_path(
        data.BUENOS_AIRES, data.LIVERPOOL)
    print "Shortest NY-NY",
    print data.shipping_map.find_path(
        data.NEW_YORK, data.NEW_YORK)

def number_of_routes():
    print "Number of routes from Liverpool-Liverpool with 3 stops or less"
    print data.shipping_map.find_paths_max_stops(
        data.LIVERPOOL, data.LIVERPOOL, 4)

    print "Number of routes from Buenos Aires-Liverpool with exactly 4 stops"
    print data.shipping_map.find_paths_exact_stops(
        data.BUENOS_AIRES, data.LIVERPOOL, 4)

    print "Number of routes from Liverpool-Liverpool with less than 26 days"
    print data.shipping_map.find_paths_days_less_than(
        data.LIVERPOOL, data.LIVERPOOL, 26)


if __name__ == '__main__':
    exact_routes()
    shortest_routes()
    number_of_routes()
