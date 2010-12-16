a = 1
b = 10.0
c = a/b
print 'a =', a, 'b =', b, 'c =', c
# alternative printing:
print 'a = %d, b = %g, c = %g' % (a, b, c)
# control of output format:
print 'a = %5.1f, b = %.5f, c = %12.4E' % (a, b, c)
# more visual demonstration of the width of the fields:
print 'a = "%5.1f", b = "%.5f", c = "%12.4E"' % (a, b, c)

