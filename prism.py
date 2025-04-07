from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
from OCC.Core.gp import gp_Pnt
from OCC.Core.gp import gp_Pnt, gp_Vec
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeFace
import math


def create_rectangular_prism(length, breadth, height):
    # Create a rectangular prism using BRepPrimAPI_MakeBox
    box = BRepPrimAPI_MakeBox(length, breadth, height).Shape()
    return box

def create_parallelogram_prism(width, height, depth, angle_deg):
    """
    Creates a parallelogram prism with the given dimensions.
    """
    angle_rad = math.radians(angle_deg)
    shift_x = height * math.tan(angle_rad)
    p1 = gp_Pnt(0, 10, 0)
    p2 = gp_Pnt(0, 10+width, 0)
    p3 = gp_Pnt(shift_x, 10+height+width, 0)
    p4 = gp_Pnt(shift_x, 10+height, 0)
    polygon = BRepBuilderAPI_MakePolygon()
    polygon.Add(p1)
    polygon.Add(p2)
    polygon.Add(p3)
    polygon.Add(p4)
    polygon.Close()
    base_face = BRepBuilderAPI_MakeFace(polygon.Wire()).Face()
    return BRepPrimAPI_MakePrism(base_face, gp_Vec(0, 0, -depth)).Shape()

def create_parallelogram_prism_opp(width, height, depth, angle_deg):
    """
    Creates a parallelogram prism with the given dimensions.
    """
    angle_rad = math.radians(angle_deg)
    shift_x = height * math.tan(angle_rad)
    p1 = gp_Pnt(0, shift_x+width+10, 0)
    p2 = gp_Pnt(0, 10+shift_x, 0)
    p3 = gp_Pnt(shift_x, 10, 0)
    p4 = gp_Pnt(shift_x, 10+width, 0)
    polygon = BRepBuilderAPI_MakePolygon()
    polygon.Add(p1)
    polygon.Add(p2)
    polygon.Add(p3)
    polygon.Add(p4)
    polygon.Close()
    base_face = BRepBuilderAPI_MakeFace(polygon.Wire()).Face()
    return BRepPrimAPI_MakePrism(base_face, gp_Vec(0, 0, -depth)).Shape()


def display_prism(box):
    # Initialize the display window
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Display the box
    display.DisplayShape(box, update=True)

    # Start the display loop
    start_display()


if __name__ == "__main__":

    length = 10.0 #change 430
    breadth = 430.0 #change 100
    height = 300.0 #change 8



    # Create the rectangular prism
    box = create_rectangular_prism(length, breadth, height)

    # Display the rectangular prism
    display_prism(box)



