#!/usr/bin/env python

def closest_colour(p, hex):

    # http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green

    r, g, b = webcolors.hex_to_rgb(hex)

    min_colours = {}

    for key, name in p.colours.items():

        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - r) ** 2
        gd = (g_c - g) ** 2
        bd = (b_c - b) ** 2
        min_colours[(rd + gd + bd)] = name

    idx = min(min_colours.keys())

    details = min_colours[idx]
    name = details['name']

    hex = p.name_to_hex(name)
    return hex, name

