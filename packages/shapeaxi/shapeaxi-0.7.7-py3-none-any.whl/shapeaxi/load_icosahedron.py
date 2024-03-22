import numpy as np

with open("neigh_indices/sphere_42_rotated_0.vtk", "r") as file:
    lines = file.readlines()

# Find the indices where different sections start
points_index = lines.index("POINTS 42 float\n")
polygons_index = lines.index("POLYGONS 80 320\n")
point_data_index = lines.index("POINT_DATA 42\n")

# Extract vertices
vertices = []
for line in lines[points_index + 1:polygons_index]:
    vertices.append(list(map(float, line.split())))

# Extract faces
faces = []
for line in lines[polygons_index + 1:point_data_index]:
    face = list(map(int, line.split()[1:]))
    faces.append(face)

# Extract point data (curvature and sulc)
curvature_data = []
sulc_data = []
for line in lines[point_data_index + 3:]:
    values = list(map(float, line.split()))
    curvature_data.append(values[0])
    sulc_data.append(values[1])

# Convert lists to numpy arrays for easier manipulation
vertices = np.array(vertices)
faces = np.array(faces)
curvature_data = np.array(curvature_data)
sulc_data = np.array(sulc_data)

# Print the results
print("Vertices:")
print(vertices)
print("\nFaces:")
print(faces)
print("\nCurvature Data:")
print(curvature_data)
print("\nSulc Data:")
print(sulc_data)
