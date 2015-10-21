# -*- coding: utf-8 -*-

import shipping
import data

def shortest_routes():
    print data.shipping_map.find_path(
        data.BUENOS_AIRES, data.LIVERPOOL)
    print data.shipping_map.find_path(
        data.NEW_YORK, data.NEW_YORK)

if __name__ == '__main__':
    shortest_routes()
