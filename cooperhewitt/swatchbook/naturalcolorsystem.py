import palette

# https://en.wikipedia.org/wiki/Natural_Color_System

class palette(palette.palette):
    
    def __init__(self):

        self.__source__ = 'naturalcolorsystem'

        self.__colours__ = {

            "#ffffff": {
                "name": "white"
            },
            "#000000": {
                "name": "black"
            },
            "#009f6b": {
                "name": "green"
            },
            "#c40233": {
                "name": "red"
            },
            "#ffd300": {
                "name": "yellow"
            },
            "#0087bd": {
                "name": "blue"
            }
        }
