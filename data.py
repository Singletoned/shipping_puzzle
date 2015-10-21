# -*- coding: utf-8 -*-

from shipping import Port, Route


LIVERPOOL = Port("Liverpool", "L")
NEW_YORK = Port("New York", "NY")
BUENOS_AIRES = Port("Buenos Aires", "BA")
CASABLANCA = Port("Casablanca", "C")
CAPE_TOWN = Port("Cape Town", "CT")

ports = set([LIVERPOOL, NEW_YORK, BUENOS_AIRES, CASABLANCA, CAPE_TOWN])

BA_NY = Route(BUENOS_AIRES, NEW_YORK, 6)
BA_C = Route(BUENOS_AIRES, CASABLANCA, 5)
BA_CT = Route(BUENOS_AIRES, CAPE_TOWN, 4)
NY_L = Route(NEW_YORK, LIVERPOOL, 4)
L_C = Route(LIVERPOOL, CASABLANCA, 3)
L_CT = Route(LIVERPOOL, CAPE_TOWN, 6)
C_L = Route(CASABLANCA, LIVERPOOL, 3)
C_CT = Route(CASABLANCA, CAPE_TOWN, 6)
CT_NY = Route(CAPE_TOWN, NEW_YORK, 8)

routes = [BA_NY, BA_C, BA_CT, NY_L, L_C, L_CT, C_L, C_CT, CT_NY]
