"""
Compute the area of an arbitrary triangle
Create a function area(vertices) that
return the area of the triangle supplied.

Test with a known triangle
"""

def area(vertices):
    xy1 = vertices[0]
    xy2 = vertices[1]
    xy3 = vertices[2]

    A = 0.5 * (xy2[0] * xy3[1] -
            xy3[0] * xy2[1] -
            xy1[0] * xy3[1] +
            xy3[0] * xy1[1] +
            xy1[0] * xy2[1] -
            xy2[0] * xy1[1])
    return A

triangle = [[0, 0], [2, 0], [2, 3]]

print area(triangle)

"""
Running program
Unix>python 2.17-area_triangle.py
3.0
"""