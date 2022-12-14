import os.path
import re

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input05.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #load input in memory coz i can
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]

picture_loaded = False
picture_as_rows = []
for line in lines:
    if not(picture_loaded) and len(line) > 0:
            # PART 1:  load in the picture
        picture_as_rows.append(line)
    elif len(line) == 0:
            # PART 2:   use the blank line in input as a place to stop and reconfigure
            #           the "picture" into a useable format
        picture_loaded = True
        picture_as_columns = []
                ## iterating from the bottom row up.  For the bottom-most (list is empty so far),
                ## each 2nd entry out of each 4 in that line is appended AS a sub list, then for 
                ## subsequent rows each 2nd entry out of each 4, nonblank, is appended TO the 
                ## appropriate sub-list
        for row in picture_as_rows[::-1]:
            if len(picture_as_columns) == 0:
                for i in range(len(row)):
                    if i % 4 == 1:
                        picture_as_columns.append([row[i]])
            else:
                for i in range(len(row)):
                    if i % 4 == 1 and row[i] != ' ':
                        picture_as_columns[i//4].append(row[i])
        ##for i in picture_as_columns:
        ##   print(i)
        ##print('\n')
    else:
            # PART 3a:  load in instruction
                ## I don't know regex.  this took forever.
        print(line)
        moves, source, dest = map(int, re.split("\D+", line)[1:])
            # PART 3b:  Use instruction, repeat
        for i in range(moves):
            moved_item = picture_as_columns[source-1].pop()
            picture_as_columns[dest-1].append(moved_item)
        ##for i in picture_as_columns:
        ##    print(i)
        ##print('\n')

    # Take last letters
answer_easy = ''        
for col in picture_as_columns:
    answer += col[-1]

print(answer_easy)
    
                    
                
                