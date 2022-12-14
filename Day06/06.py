import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input06.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #load input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]

# PROBLEM START #########################################

line = lines[0]

def all_unique(string):
    unq = []
    for i in string:
        if i not in unq:
            unq += i
        else:
            break
    return len(unq) == len(string)

    
def star_1():
    cur_index = 4
    marker_found = False
    while not marker_found:
        segment = line[cur_index-4 : cur_index]
        if all_unique(segment):
            marker_found = True
            answer_1 = cur_index
        cur_index += 1

    print(f'Star 1: {answer_1}')

def star_2():    
    cur_index = 14
    marker_found = False
    while not marker_found:
        segment = line[cur_index-14 : cur_index]
        if all_unique(segment):
            marker_found = True
            answer_2 = cur_index
        cur_index += 1

    print(f'Star 2: {answer_2}')
    


def main():
        star_1()
        star_2()

if __name__ == "__main__":
    main()

    



        
        
    
