from scitools.Lumpy import Lumpy

lumpy = Lumpy() 
from numpy import zeros
B = zeros((100,20))
c = B[-1,-1]
del zeros
lumpy.object_diagram()

