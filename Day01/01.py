import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input01.txt'
    ## update file name above
input_file_path = this_folder + input_filename


totals = []
current_total = 0

fileline = 0

with open(input_file_path, "r") as infile:
    lines = infile.readlines()

    
for calories in lines:
    #fileline += 1
    if calories == '\n':
        totals.append(current_total)
        current_total = 0
    else:
        #print(calories)
        calories_numeric = int(calories[:len(calories)-1])
        current_total += calories_numeric
current_total += calories_numeric




#answer 1
print(max(totals))

#answer 2
top_three = 0
for _ in range(3):
    top_three += max(totals)
    totals.remove(max(totals))
print(top_three)


