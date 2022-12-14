import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input09.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]
    
    
def move(point, vector):
    dpad = {'U': [0, 1], 'R': [1, 0], 'D': [0, -1], 'L': [-1, 0]}
    if vector in list(dpad.keys()):
        vector = dpad[vector]
    point[0] = int(point[0] + vector[0])
    point[1] = int(point[1] + vector[1])
    
def follow(H, T):
    diff = [H[0] - T[0], H[1] - T[1]]
    abs_diff = [abs(diff[0]), abs(diff[1])]
    if max(abs_diff) <= 1:
        return
        ## get indexes of larger and smaller diff, store as variables.
    large_dim, small_dim = [0, 1] if abs_diff[0] > abs_diff[1] else [1, 0]
    diff[large_dim] /= 2
    move(T, diff)
        
T = [0, 0]
H = [0, 0]

visited = [[0, 0]]

#test = 0
for line in lines:
    #test += 1
    #if test > 100:
    #    break
    direction, steps = line.split(' ')
    steps = int(steps)
    #test += steps
    for i in range(steps):
        move(H, direction)
        follow(H, T)
        print(H, T)
        if T not in visited:
            visited.append(T.copy())

print(len(visited))
        
    

