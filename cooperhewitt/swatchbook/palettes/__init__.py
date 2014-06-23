def palettes():

    # Generate this dynamically by reading dir?

    return [
        'css3',
        'css4'
    ]

def load_palette(reference):

    palette = __import__(reference)
    return palette.colours()

if __name__ == '__main__':

    p = load_palette('css4')
    print p
    
    
