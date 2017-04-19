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

add_sphere(edges, 250, 250, 0, 150, .1)
matrix_mult(make_rotY(math.pi/2), edges)

draw_polygons(edges, screen, color)

display(screen)
