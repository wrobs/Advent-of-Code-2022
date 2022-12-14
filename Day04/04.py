import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input04.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]

total_easy = 0
total_hard = 0
for line in lines:
    r1, r2 = map(str, line.split(','))
    r1 = [int(i) for i in r1.split('-')]
    r2 = [int(i) for i in r2.split('-')]
    full = r1 + r2
    
    if ((r1[0] <= r2[0] and r1[1] >= r2[1]) or 
        (r2[0] <= r1[0] and r2[1] >= r1[1])):
        
        total_easy += 1
    
    if not(r1[0] == min(full) and r1[1] < r2[0] or
        r2[0] == min(full) and r2[1] < r1[0]):
        
        total_hard += 1
        
print(total_easy)
print(total_hard)