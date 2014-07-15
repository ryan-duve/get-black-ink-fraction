#!/usr/bin/python
#fraction-black.py
#takes a black and white picture and returns fraction that is black
#run with 'python fraction-black.py FILENAME.dat'

import Image
import sys #for command line argument

im=Image.open(sys.argv[1])

print im.getcolors()

black=im.getcolors()[1][0]
white=im.getcolors()[0][0]

fblack=float(black)
fwhite=float(white)

print 'black =',fblack
print 'white =',fwhite

print fblack/(fblack+fwhite)
