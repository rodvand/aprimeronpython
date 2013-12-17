"""
3.14
"""
import sys
try:
    C = float(sys.argv[1])
except IndexError:
    print 'C must be provided as command-line argument'
    sys.exit(1)
