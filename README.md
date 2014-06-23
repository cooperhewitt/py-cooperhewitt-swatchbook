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

	# See below for object methods

### Object methods

Assuming:

	palette = cooperhewitt.swatchbook.naturalcolorsystem.palette()

#### palette.souce()

	print palette.source()

	# Would print:
	# naturalcolorsystem

#### palette.colours()

	print palette.colours()

	# Would print
	# {'#009f6b': {'name': 'green'}, '#c40233': {'name': 'red'}, '#000000': {'name': 'black'}, '#0087bd': {'name': 'blue'}, '#ffd300': {'name': 'yellow'}, '#ffffff': {'name': 'white'}}

#### palette.hex(<NAME>)

	print palette.hex('red')

	# Would print:
	# #c40233

#### palette.name(<HEX>)

	print palette.name('#ffd300')

	# Would print:
	# yellow

#### palette.as_dict()

Return colours and source as a Python dict object.

	print palette.as_dict()

	# Would print:
	# {'colours': {'#009f6b': {'name': 'green'}, '#c40233': {'name': 'red'}, '#000000': {'name': 'black'}, '#0087bd': {'name': 'blue'}, '#ffd300': {'name': 'yellow'}, '#ffffff': {'name': 'white'}}, 'source': 'naturalcolorsystem'}

#### palette.as_json(<KWARGS>)

Return the results of `palette.as_dict` serialized as JSON.

	print palette.as_json(indent=2)

	# Would print:
	# {
	#   "colours": {
	#     "#009f6b": {
	#       "name": "green"
	#     }, 
	#     "#c40233": {
	#       "name": "red"
	#     }, 
	#     "#000000": {
	#       "name": "black"
	#     }, 
	#     "#0087bd": {
	#       "name": "blue"
	#     }, 
	#     "#ffd300": {
	#       "name": "yellow"
	#     }, 
	#     "#ffffff": {
	#       "name": "white"
	#     }
	#   }, 
	#   "source": "naturalcolorsystem"
	# }
	
#### palette.sorted()

Return the hex colours sorted.
    
	print palette.sorted()

	# Would print:
	# ['#ffd300', '#009f6b', '#0087bd', '#c40233', '#000000', '#ffffff']

#### palette.closest(<HEX>)

	print palette.closest('#7c5d5c')

	# Would print
	# ('#c40233', 'red')

## Palettes

The following colour palettes are supported:

* [crayola](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/blob/master/cooperhewitt/swatchbook/crayola.py)
* [css3](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/blob/master/cooperhewitt/swatchbook/css3.py)
* [css4](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/blob/master/cooperhewitt/swatchbook/css4.py)
* [naturalcolorsystem](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/blob/master/cooperhewitt/swatchbook/naturalcolorsystem.py)

