meters = 640 # Meters we want to convert
inch = .0254 # In meter 
foot = 12 * inch 
yard = 3 * foot 
mile = 1760 * yard

print("""%g meters is 
in inches: %g
in feet: %g
in yards: %g
in miles: %g""" % (meters, meters / inch, meters / foot, meters / yard, meters / mile))

"""
Running the program
Unix>python length_conversion.py
640 meters is 
in inches: 25196.9
in feet: 2099.74
in yards: 699.913
in miles: 0.397678
"""
