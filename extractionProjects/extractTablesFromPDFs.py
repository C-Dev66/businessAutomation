"""
Description:

This python script will be able to extract tables from a pdf located in the same
working directory with pandas library.

In order to this we will be using the camelot-py library
official documentation can be found at the following:
https://camelot-py.readthedocs.io/en/master/

pip3 install camelot-py
pip3 install tk
pip3 install ghostscript


after installing you will need to also add the two dependencies
1.
2.


"""

import camelot

from ctypes.util import find_library
find_library("gs")
import tkinter

tables = camelot.read_pdf('foo.pdf', pages='1')

print(tables)

# Issues with ghostscript still persist
