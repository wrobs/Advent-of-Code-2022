import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input02.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]
lines = [s.replace(' ', '') for s in lines]

    
    # prep variables, rock paper scissors

## (the number of combinations is small enough thet it is
## faster to calculate all possible results and then key-match
## them to the input, rather than calc for each input line)    
results = {}
p1_shapes = [['A', 1], ['B', 2], ['C', 3]]
p2_shapes = [['X', 1], ['Y', 2], ['Z', 3]]

# results dictionary for easy star, xyz = rock paper scissors
for i in p1_shapes:
    for j in p2_shapes:
            ##add my shape value to result of play
        result = j[1]
            ## tie is +3, win (paper beats rock etc) is +6
        if i[1] == j[1]:
            result += 3
        elif (j[1] - i[1]) % 3 == 1:
            result += 6
        results[i[0] + j[0]] = result

# results dictionary for hard star, xyz = lose draw win
results2 = {}
for i in p1_shapes:
    for j in p2_shapes:
        if j[0] == 'X':
            offset = 2
        elif j[0] == 'Y':
            offset = 0
        elif j[0] == 'Z':
            offset = 1
            ## get p2's move using offset and modulo, and get score 
            ## from the result dictionary obtained for the easy star, 
            ## then append that to new results dictionary
        p2_move = p2_shapes[(i[1] - 1 + offset) % 3]
        combo = i[0] + p2_move[0]
        result2 = results[combo]
        results2[i[0] + j[0]] = result2
        
        

    # Start at zero and run game (easy)
total_score = 0
for line in lines:
    total_score += results[line]
print(total_score)

    # Start at zero and run game (hard)
total_score = 0
for line in lines:
    total_score += results2[line]
print(total_score)   
    




