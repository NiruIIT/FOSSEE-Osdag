from OCC.Core.gp import gp_Vec, gp_Trsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Display.SimpleGui import init_display

# Import functions from existing scripts
from Isection import create_i_section
from prism import create_rectangular_prism, create_parallelogram_prism, create_parallelogram_prism_opp


#positioning the model in coordinate system
from OCC.Core.gp import gp_Ax1, gp_Pnt, gp_Dir
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform

# Define rotation axis (Y-axis)
rotation_axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0))

# Rotate 90 degrees = π/2 radians
trsf_rotate = gp_Trsf()
trsf_rotate.SetRotation(rotation_axis, 3.14159 /2)  # 90 degrees


# Create and position main structure
length, width, depth = 6100.0, 100.0, 200.0 # Column height + 2*batten_thickness (6100+(2*10))
flange_thickness, web_thickness = 10.0, 6.0
batten_width, batten_depth, batten_thickness = 470.0, 300.0, 10.0
lace_width, lace_depth, lace_spacing = 430.0, 100.0, 430.0

#I-sections creation and postiioning
i_section_1 = create_i_section(length, width, depth, flange_thickness, web_thickness)
i_section_2 = create_i_section(length, width, depth, flange_thickness, web_thickness)
trsf = gp_Trsf()
trsf.SetTranslation(gp_Vec(0, 350, 0))
i_section_2_transformed = BRepBuilderAPI_Transform(i_section_2, trsf, True).Shape()

#Battens creation and positioning
bottom_batten = create_rectangular_prism(batten_thickness, batten_width, batten_depth)
top_batten = create_rectangular_prism(batten_thickness, batten_width, batten_depth)

trsf_bottom = gp_Trsf()
trsf_bottom.SetTranslation(gp_Vec(0, (450-batten_width)/2, (depth - batten_depth)/2))
bottom_batten_transformed = BRepBuilderAPI_Transform(bottom_batten, trsf_bottom, True).Shape()

trsf_top = gp_Trsf()
trsf_top.SetTranslation(gp_Vec(length-10, (450-batten_width)/2, (depth - batten_depth)/2))
top_batten_transformed = BRepBuilderAPI_Transform(top_batten, trsf_top, True).Shape()

#Horizontal laces creation and positioning
laces = []
n = int(length / lace_spacing)
for i in range(0, n+1):
    if i == n:  # this condition is used to make fit the the last batten withing the frame by decreasing the depth of the last lace
        lace = create_rectangular_prism(80, lace_width, 8)
        trsf_lace3 = gp_Trsf()
        trsf_lace3.SetTranslation(gp_Vec(i * lace_spacing, (450 - lace_width) / 2, -8))
        trsf_lace4 = gp_Trsf()
        trsf_lace4.SetTranslation(gp_Vec(i * lace_spacing, (450 - lace_width) / 2, depth))
        laces.append(BRepBuilderAPI_Transform(lace, trsf_lace3, True).Shape())
        laces.append(BRepBuilderAPI_Transform(lace, trsf_lace4, True).Shape())
    else:
        lace = create_rectangular_prism(lace_depth, lace_width, 8)
        trsf_lace1 = gp_Trsf()
        trsf_lace1.SetTranslation(gp_Vec(i * lace_spacing, (450 - lace_width) / 2, -8))
        trsf_lace2 = gp_Trsf()
        trsf_lace2.SetTranslation(gp_Vec(i * lace_spacing, (450 - lace_width) / 2, depth))

        laces.append(BRepBuilderAPI_Transform(lace, trsf_lace1, True).Shape())
        laces.append(BRepBuilderAPI_Transform(lace, trsf_lace2, True).Shape())

# Inclined laces creation and positioning
x = 100
inclined_laces = []
for i in range(0, int(length / lace_spacing)):
    prism = create_parallelogram_prism(100, 330, 8, 45)
    trsf1 = gp_Trsf()
    trsf1.SetTranslation(gp_Vec(x, 0, 0))
    transformed_prism1 = BRepBuilderAPI_Transform(prism, trsf1, True).Shape()
    
    prism_opp = create_parallelogram_prism_opp(100, 330, 8, 45)
    trsf2 = gp_Trsf()
    trsf2.SetTranslation(gp_Vec(x, 0, depth+8))
    transformed_prism2 = BRepBuilderAPI_Transform(prism_opp, trsf2, True).Shape()

    x +=lace_spacing
    inclined_laces.append(transformed_prism1)
    inclined_laces.append(transformed_prism2)

# Combine all parts into one model
structure = BRepAlgoAPI_Fuse(i_section_1, i_section_2_transformed).Shape()
structure = BRepAlgoAPI_Fuse(structure, bottom_batten_transformed).Shape()
structure = BRepAlgoAPI_Fuse(structure, top_batten_transformed).Shape()
for lace in laces:
    structure = BRepAlgoAPI_Fuse(structure, lace).Shape()
for inclined_lace in inclined_laces:
    structure = BRepAlgoAPI_Fuse(structure, inclined_lace).Shape()



# Apply rotation to entire structure
structure_rotated = BRepBuilderAPI_Transform(structure, trsf_rotate, True).Shape()

# Initialize display
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(structure_rotated, update=False)
display.FitAll()
display.Repaint()
start_display()




