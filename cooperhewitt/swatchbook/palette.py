import json
import webcolors
import colorsys
from colormath.color_objects import RGBColor

class palette:

    def __init__(self):

        self.source = None
        self.colours = None

    def __str__(self):
        return self.as_json(indent=2)

    def source(self):
        return self.__source__

    def colours(self):
        return self.__colours__

    def colors(self):
        return self.colours()

    def as_dict(self):

        return {
            'source': self.source(),
            'colours': self.colours()
        }

    def as_json(self, **kwargs):

        return json.dumps(self.as_dict(), **kwargs)

    def name(self, hex):

        hex = hex.lower()

        details = self.__colours__.get(hex, None)

        if not details:
            raise Exception("Invalid hex colour")

        return details['name']

    def hex(self, name):

        for hex, details in self.__colours__.items():

            if details['name'].lower() == name.lower():
                return hex

        raise Exception("Invalid colour name")

    def sorted(self):

        colours = self.colours()
        colours = colours.keys()

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

    def closest(self, hex):

        # http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green

        r, g, b = webcolors.hex_to_rgb(hex)

        min_colours = {}

        for key, details in self.colours().items():

            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - r) ** 2
            gd = (g_c - g) ** 2
            bd = (b_c - b) ** 2
            min_colours[(rd + gd + bd)] = details

        idx = min(min_colours.keys())

        details = min_colours[idx]
        name = details['name']

        hex = self.hex(name)
        return hex, name

    def closest_delta_e(self, hex):
        """
        Calculates the Delta E difference between a hex value and others in
        the specified palette and returns the closest match (CMC method)
        http://en.wikipedia.org/wiki/Color_difference#CMC_l:c_.281984.29
        """
        incumbent = RGBColor(*webcolors.hex_to_rgb(hex))

        shortest_dist = None
        nearest_colour = None
        for key, details in self.colours().items():

            candidate = RGBColor(*webcolors.hex_to_rgb(key))
            cdist = incumbent.delta_e(candidate, method="cmc")
            if nearest_colour is None:
                nearest_colour = (candidate, key, details)
                shortest_dist = cdist
            elif cdist < shortest_dist:
                shortest_dist = cdist
                nearest_colour = (candidate, key, details)

        details = nearest_colour[2]
        name = details['name']
        hex = self.hex(name)
        return hex, name
