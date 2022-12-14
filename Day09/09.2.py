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
    if abs_diff[small_dim] == 2:
        diff[small_dim] /= 2
    move(T, diff)
        
#followers = [[0, 0]] * 9
followers = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
H = [0, 0]

visited = [[0, 0]]

#def strrep(string, index, new):
#    newstring = ''
#    newstring = string[:index] + new
#    if index < len(string) - 1:
#        newstring += string[index+1: len(string)]
#    return newstring
#
#def printmap(tails, head):
#    i = 9
#    minx = min([x[0] for x in tails+[head]+[[0,0]]])
#    miny = min([x[1] for x in tails+[head]+[[0,0]]])
#    maxx = max([x[0] for x in tails+[head]+[[0,0]]])
#    maxy = max([x[1] for x in tails+[head]+[[0,0]]])
#    grid = []
#    for i in range(miny, maxy+1):
#        grid.append('.' * (maxx-minx+1))
#    for p in range(8, -1, -1):
#        grid[tails[p][1] - miny] = strrep(grid[tails[p][1] - miny], tails[p][0] - minx,  str(p+1))
#    grid[-miny] = strrep(grid[-miny], -minx , 'S')
#    grid[head[1] - miny] = strrep(grid[head[1] - miny], head[0] - minx , 'H')
#    for i in grid[::-1]:
#        print(i)
    
        
    
    
#test = 0
#t= 0
for line in lines:
    #test += 1
    #if test > 10:
    #    break
    #print(test)
    direction, steps = line.split(' ')
    
    steps = int(steps)
    #print('\n', direction, steps)
    #t+= steps
    for i in range(steps):
        move(H, direction)
        follow(H, followers[0])
        for j in range(len(followers)-1):
            follow(followers[j], followers[j+1])
        #print(H, followers)        
        if followers[8]  not in visited:
            visited.append(followers[8].copy())
        #if(line =='U 8'):
        #    printmap(followers, H)
        #    print('\n')
    #print(followers+[H]+[[0,0]])
    #printmap(followers, H)
    
#print(visited)

print(len(visited))
#print(t)

    

