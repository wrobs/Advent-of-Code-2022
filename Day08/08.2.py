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
    
    ## get list of scores looking 1 way
def score_1way(nums):
    max = -1
    scores = []
    for i in range(len(nums)-1):
        cur_score = 0
        for j in range(i+1, len(nums)):
            cur_score += 1
            if nums[j] >= nums[i]:
                break
        scores.append(cur_score)
    scores.append(0)
    return scores
    
    ## get list looking both ways
def score(nums):
    score_right = score_1way(nums)
    score_left = score_1way(nums[::-1])[::-1]
    score_product = [n1 * n2 for n1, n2 in zip(score_left, score_right)]
    return score_product

    ## get row-wise score
answer_grid = []
for row in lines:
    answer_grid.append(score(row))
  
for j in range(len(lines[0])):
    col = [row[j] for row in lines]
    answer_col = score(col)
    for i in range(len(answer_col)):
        answer_grid[i][j] *= answer_col[i]

ans = 0
for row in answer_grid:
    if max(row) > ans:
        ans = max(row)


print(ans)
    
    
    
    
        
    