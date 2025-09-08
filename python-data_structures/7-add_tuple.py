#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    padded_a = tuple_a + (0, 0)
    padded_b = tuple_b + (0, 0)
    return (padded_a[0] + padded_b[0], padded_a[1] + padded_b[1])
