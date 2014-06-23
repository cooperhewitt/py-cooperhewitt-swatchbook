import importlib

def palettes():

    # Generate this dynamically by reading dir?

    return [
        'css3',
        'css4'
    ]

def load_palette(reference):
    pkg = "cooperhewitt.swatchbook.%s" % reference
    mod = importlib.import_module(pkg)
    return mod.palette()
    
def closest(reference, hex):
    palette = load_palette(reference)
    return palette.closest(hex)

if __name__ == '__main__':

    import sys

    ref = sys.argv[1]
    hex = sys.argv[2]
    
    print closest(ref, hex)

    p = load_palette(ref)
    print p.sort()

