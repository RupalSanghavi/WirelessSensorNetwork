import sys

# def create_list:
#     for i in pairs:
#         adj_list.setdefault(i[0], []) #create list for values
#         adj_list.setdefault(i[1], []) #create list for values
#         adj_list[i[0]].append(i[1])
#         adj_list[i[1]].append(i[0])
#     return
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
print lines[0].split()
