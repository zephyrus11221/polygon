from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

'''
parse_file( 'script', edges, transform, screen, color )
'''
'''
add_sphere(edges,0,0,0, 150, .1)
add_sphere(edges,0,0,0, 150, .05)
'''

add_torus(edges, 0, 0, 0, 50, 200, .1)

matrix_mult(make_rotX(math.pi/4), edges)
matrix_mult(make_rotY(math.pi/4), edges)
matrix_mult(make_translate(250, 250, 0), edges)

draw_polygons(edges, screen, color)

display(screen)
