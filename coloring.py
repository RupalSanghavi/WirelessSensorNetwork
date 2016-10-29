import sys

def read_file(lines):
    with open(sys.argv[1], "r") as file:
        for line in file:
            if "S" in line:
                break
        for line in file:
            lines.append(line)
            #print(line)
lines = []
read_file(lines)
coordinates = lines[0].split()
print coordinates
adj_list = {}
for line in lines:
    coordinates = line.split()
    center_vertice = [coordinates[0]]
    center_vertice.append(coordinates[1])
    for adjacent_vertex in coordinates[2:]:
        #data = [1,2,3,4,5,6]
        for i,k in zip(coordinates[0::2], coordinates[1::2]):
            adj_list['check'] = [i,k]
