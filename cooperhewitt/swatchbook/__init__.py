#!/usr/bin/env python

import colorsys
import webcolors
import json
import sys

class swatchbook:

    def __init__(self, path):

        fh = open(path, 'r')
        data = json.load(fh)

        self.source = data['source']
        self.colours = data['colours']

    def name_to_hex(self, name):

        for hex, details in self.colours.items():

            if details['name'] == name:
                return hex

        return None

    def merge(self, palette):

        sources = []
        colours = {}

        sources.append(self.source)

        if not palette.source in sources:
            sources.append(palette.source)

        for hex, details in self.colours.items():
            details['source'] = self.source
            colours[hex] = details

        for hex, details in palette.colours.items():

            if not colours.get(hex):
                details['source'] = palette.source
                colours[hex] = details

        self.source = ';'.join(sources)
        self.colours = colours

        # how exactly...
        # return palette(new)

    def sort_colours(self):

        colours = []

        for hex, ignore in self.colours.items():
            colours.append(hex)

        colours = map(webcolors.hex_to_rgb, colours)

        def hsl(x):
            to_float = lambda x : x / 255.0
            (r, g, b) = map(to_float, x)
            h, s, l = colorsys.rgb_to_hsv(r,g,b)
            h = h if 0 < h else 1 # 0 -> 1
            return h, s, l

        def yqi(x):
            to_float = lambda x : x / 255.0
            (r, g, b) = map(to_float, x)
            y, i, q = colorsys.rgb_to_yiq(r,g,b)
            y = y if 0 < y else 1 # 0 -> 1
            return y, q, i

        colours = sorted(colours, key=hsl)
        colours = map(webcolors.rgb_to_hex, colours)

        return colours

    def dump(self, fh=sys.stdout):

        out = {
            'source': self.source,
            'colours': self.colours
            }
           
        json.dump(out, fh, indent=2)


if __name__ == '__main__':

    import sys

    path = sys.argv[1]
    hex = sys.argv[2]

    p = palette(path)
    u = utils(p)

    c_hex, c_name = u.closest_colour(hex)

    print hex
    print c_hex
    print c_name
