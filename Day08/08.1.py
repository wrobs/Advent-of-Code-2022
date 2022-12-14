import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input08.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]
    
# PROBLEM START ########################################

for i in range(len(lines)):
    lines[i] = [int(n) for n in lines[i]]
    
    ## get visibility of a list from either end
def visible(nums):
    max = -1
    bools = []
        ## from left
    for n in (nums):
        if n > max:
            max = n
            bools.append(1)
        else:
            bools.append(0)
        ## from right
    max = -1
    j = 1        
    for n in nums[::-1]:
        if n > max:
            max = n
            bools[-j] = 1
        j+=1
    return bools
    
    ## get row-wise visibility
answer_grid = []
for row in lines:
    answer_grid.append(visible(row))
   
for j in range(len(lines[0])):
    col = [row[j] for row in lines]
    
        ## from up or down
    answer_col = visible(col)
    
        ## merge 1s to grid
    for i in range(len(answer_col)):
        if answer_col[i] == 1:
            answer_grid[i][j] = 1


    ##
ans = 0
for row in answer_grid:
    ans += sum(row)

print(ans)
    
    
    
    
        
    