"""
Ask the user for a temperature in Fahrenheit
Compute the corresponding temperature in Celsius
Print it
"""
def f2c(c):
    return (c-32)*5./9.

input = raw_input("Give me the temperature in Fahrenheit...\n")
print "The temperature is %d in Celsius" % f2c(int(input))

"""
Running program
Unix>python 3.1-f2c_qa.py
Give me the temperature in Fahrenheit...
32
The temperature is 0 in Celsius
"""
