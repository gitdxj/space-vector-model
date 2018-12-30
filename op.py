# -*- coding: utf-8 -*-
def and_op(list_a, list_b):
    return list(set(list_a).intersection(set(list_b)))


def or_op(list_a, list_b):
    return list(set(list_a).union(set(list_b)))


def dif_op(list_a, list_b):
    return list(set(list_a).difference(set(list_b)))

