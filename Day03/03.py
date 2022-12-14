import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input03.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]

    # a letter's "Priority" is it's index (starting at 1) in the alphabet. +26 for uppercase
priorities = 'abcdefghijklmnopqrstuvwxyz'
prioritiesU = priorities.upper()
priorities = '-' + priorities + prioritiesU

    # separate halves and find a match, add matching letters index in alphabet to total
total = 0
for bag in lines:
    cpt1 = bag[:int(len(bag)/2)]
    cpt2 = bag[int(len(bag)/2):]
    found = False
    for i in cpt1:
        for j in cpt2:
            if i==j:
                total += priorities.index(i)
                found = True
                break
        if found:
            break
    
print(f'star one: {total}')    

 # Star 2: find item in all three lines, every three lines

total = 0
set_of_3 = []
for bag in lines:
    if len(set_of_3) != 3:
        set_of_3.append(bag)
    else:
        print(set_of_3)
        found = False
        for i in set_of_3[0]:
            if i in set_of_3[1] and i in set_of_3[2]:
                total += priorities.index(i)
                print(i)
                print('\n')
                found = True
                break
        if found == False:
            print('###########################################################################')
        set_of_3 = [bag]
                

print(f'star two: {total}')    

    
['FnjQnsqsFTnStvplhhzzFS', 'TBHHCsgVRRcMHbLR', 'GcLdGBJvBvLJHccJBvqHpGzDFfzwfzjwhDwrSFpfpDSn']



