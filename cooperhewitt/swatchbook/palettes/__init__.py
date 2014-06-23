def palettes():

    return [
        'css3',
        'css4'
    ]

def load_palette(reference):

    if not reference in palettes():
        raise Exception, "Invalid palette"

    # Please figure out the hoo-hah to make dynamic
    # loading work (20140623/straup)

    if reference == 'css3':
        import css3
        return css3.colours()
    
if __name__ == '__main__':

    p = load_palette('css5')
    print p
    
    
