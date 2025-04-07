# FOSSEE-Osdag
OSDAG PROJECT 
DOCUMENTATION:
 
Task 1 :  
•	Objective:   Create a shear force (SFD) and bending moment diagram (BMD) from the values provided in the Excel sheet using PyPlot.
•	Explanation of Code : 
1.	The code starts by importing necessary libraries: pandas for data handling and matplotlib for plotting.
2.	`read_excel_data(file_path)` function attempts to read an Excel file and return its data as a DataFrame. If reading fails, it returns None.
3.	`plot_diagrams(df)` function:
-	Takes the DataFrame as input and creates a side-by-side plot for BMD and SFD.
-	It uses vertical lines (`vlines`) to indicate force/moment magnitudes at each distance.
-	It fills under the curves for visual emphasis.
-	Plots the actual lines and marks them with points (`marker='o'`).
-	Annotates the maximum and minimum values for both BMD and SFD with arrows and labels.
4.	`main () ` function:
-	Specifies the path to the Excel file.
-	Reads the data and plots the diagrams.
5.	If executed as a script, the main function is called.


•	Generated diagrams: 
 

Task 2:  
📐3D Structural Modeling Using PythonOCC

•	Objective:  Develop a CAD drawing with PythonOCC of a Laced Compound Column as shown in the representative image.

🧱 Overview:   This project creates a complete 3D model of a structural frame using I-sections, horizontal battens, horizontal laces, and inclined parallelogram laces using the PythonOCC CAD modeling library (a Python wrapper for OpenCASCADE).
The structure mimics a steel truss or lattice frame used in industrial or civil applications, allowing for strong yet lightweight support.

🗂 File Structure:
├── Isection.py                  # Generates the I-section geometry
├── prism.py                    # Generates various prism geometries
├── task2.py                    # Assembles and visualizes the full structure

📏 Components Breakdown: 

a.	I-section Generation
The `create_i_section` function generates an I-shaped cross-sectional beam. This function uses the BRepPrimAPI module to create individual parts (flanges and web) and combines them using BRepAlgoAPI_Fuse to form a solid I-section.
Key parameters:
- Length, width, depth of the I-section
- Flange and web thickness
- The top flange is vertically offset to sit above the bottom flange and web.

b.	Prism Shapes
Functions are defined to create standard and custom prism geometries:
- `create_rectangular_prism` creates a standard box shape using given dimensions. Used to produce the horizontal laces.
- `create_parallelogram_prism` and `create_parallelogram_prism_opp` create inclined laces in parallelogram shapes with specific angle and shift. Used to create inclined laces and fit it in between two horizontal laces.

🏗️ Main Assembly - task2.py
This is the main script that constructs the full structural frame by fusing individual parts and applying necessary transformations.
🧩 Steps:
a. I-section Creation
•	Creates two vertical columns (i_section_1, i_section_2)
•	Second column is translated along Y-axis (350mm)
b. Horizontal Battens
•	Top and bottom battens are placed at both ends between columns
•	Created using create_rectangular_prism
c. Horizontal Laces
•	Positioned at equal intervals (lace_spacing)
•	Placed both above and below the I-beam structure
d. Inclined Laces
•	Created using parallelogram prisms
•	Alternating directions (create_parallelogram_prism, create_parallelogram_opp)
•	Connected diagonally between two I-sections
e. Model Fusion
All components are combined using BRepAlgoAPI_Fuse.
f. Rotation
•	Structure is rotated by -90° around the Z-axis using gp_Trsf.


🎨 Visualization:
The final structure is displayed using the `init_display()` method from `OCC.Display.SimpleGui`. All shapes are rendered and fitted in the viewport using `display.DisplayShape()` and `display.FitAll()`.


✅ Output
•	A 3D CAD model of a double I-section structure with full horizontal and inclined bracing.
•	Visually interactive display (zoom/pan/rotate).

 
   



🛠️ Dependencies
•	PythonOCC-core
•	OpenCASCADE (through PythonOCC)
•	math, OCC.Core.gp, OCC.Core.BRep* modules





