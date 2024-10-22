#!/usr/bin/env python3

import collections

def read_json(filename):
    raise NotImplementedError


def calc_distance_matrix(node_list):
    raise NotImplementedError


PolarCoordinate = collections.namedtuple('PolarCoordinate', ['r', 'phi'])
Node = collections.namedtuple('Node', ['id', 'polar_coordinate'])

def calc_polar_coordinates(depot, node_list):
    raise NotImplementedError


def order(p):
    raise NotImplementedError

