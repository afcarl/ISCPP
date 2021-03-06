#!/usr/bin/env python3

"""
plotsunspots.py : plot sunspot data from spreadsheet

Copyright (C) Simon D. Levy 2016

This file is part of ISCPP.

ISCPP is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
"""

# These packages will do most of our work for us
from numpy import *
from matplotlib.pyplot import *

# Load the sunspot data into a NumPy array
a = loadtxt("sunspots-no-header.csv", delimiter=",")

# The first column is the year
year = a[:,0]

# The second column in the month
month = a[:,1]

# The third column is the sunspots
spots = a[:,2]

# Compute the date
time = year + (month - .5) / 12

# Build the plot 
plot(time, spots)

# Add annotations
xlabel('Year')
ylabel('# of Sunspots')
title('Sunspot Counts')

# Show it!
show()
