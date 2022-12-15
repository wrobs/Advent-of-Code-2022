import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input10.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory


# START ##################

with open(input_file_path, "r") as infile:
    line = infile.readline().replace('\n', '')
    key_strengths = 0
    #print(line)
    strength = 0
    x = 1
    step = 1
    wait = False
    scanlines = [[],[],[],[],[],[],[]]
    while line:
        row = (step-1)// 40
        sprite = (step-1) % 40
        if abs(x-sprite) < 2:
            scanlines[row].append('#')
        else:
            scanlines[row].append(' ')
        if step % 40 == 20:
            strength = x*step
            key_strengths += strength
        #print('step: ', step, ', line: ', line, ', x: ', x, ', ans: ', strength, ', answer:', key_strengths)
        if not wait:
            line = line.split(' ')
        cmd = line[0]
        if len(line) == 2:
            num = int(line[1])
            wait = not wait
            if not wait:
                x += num
        step += 1
        if not wait:
            line = infile.readline().replace('\n', '')
            

            
print(key_strengths)
for i in scanlines:
    print(''.join(i))
        
    
            
        
        