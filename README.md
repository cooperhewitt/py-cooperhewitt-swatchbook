# py-cooperhewitt-swatchbook

Cooper Hewitt's Python tools for wrangling colours.

## Usage

### Simple usage

	import cooperhewitt.swatchbook as sb
	print sb.closest('css3', '#7c5d5c')

	# Would print:
	# ('#696969', 'dimgrey') 

### Less-simple usage

	import cooperhewitt.swatchbook as sb

	palette = sb.load_palette('crayola')
	print palette.name('#a8e4a0')

	# Would print:
	# Granny Smith Apple

### Even-less-simple usage

	import cooperhewitt.swatchbook.crayola

	palette = cooperhewitt.swatchbook.crayola.palette()

	print palette.source()

	print palette.colours()

	print palette.hex(<NAME>)

	print palette.name(<HEX>)

	print palette.as_dict()

	print palette.as_json()
    
	print palette.sorted()

	print palette.closest(<HEX>)

## Palettes

The following colour palettes are supported:

* crayola
* css3
* css4
* naturalcolorsystem

