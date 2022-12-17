import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input11.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory


# classes and functions ####################
    ## example: Monkey( inhand = [12, 13, 14],
    ##                  operation = 'old * 4'
    ##                  test = 19
    ##                  receiver = [0, 2] )
class Monkey:
    def __init__(self, inhand = None, operation = None, test = None, receiver = None):
        self.inhand = inhand if inhand is not None else []
        self.operation = operation
        self.test = test
        self.receiver = receiver if receiver is not None else [None, None]
    
    def update_worry(self):
        self.inhand = [eval(self.operation) // 3 for old in self.inhand]
    
    def throw(self, lineup):
        t = []
        f = []
        for i in range(len(self.inhand)):
            if self.inhand[i] % self.test == 0:
                t.append(self.inhand[i])
            else:
                f.append(self.inhand[i])
        self.inhand = []
        lineup[self.receiver[0]].inhand.extend(t)
        lineup[self.receiver[1]].inhand.extend(f)
        
    
# build Monkeys ########################################

monkeys = []

with open(input_file_path, "r") as infile:
    
    line = infile.readline().replace('\n', '') #monkey 0
    while line:
        line = infile.readline().replace('\n', '') #inhand
        line = line.replace('  Starting items: ', '')
        new_vals = [int(x) for x in line.split(', ')]

        line = infile.readline().replace('\n', '') #operation
        new_op = line[(line.find('=') + 1):]

        line = infile.readline().replace('\n', '') #test
        new_test = int(line.replace('  Test: divisible by ', ''))

        line = infile.readline().replace('\n', '') #iftrue
        reciever_T = int(line.replace('    If true: throw to monkey ', ''))
        line = infile.readline().replace('\n', '') #iffalse
        reciever_F = int(line.replace('    If false: throw to monkey ', ''))

        new_monkey = Monkey(new_vals, new_op, new_test, [reciever_T, reciever_F])
        
        monkeys.append(new_monkey)
    
        line = infile.readline().replace('\n', '') #blank
        line = infile.readline().replace('\n', '') #nextmonkey

# run simianlation ###############################################

tallies = []

for _ in range(20):
    for i in range(len(monkeys)):
        monkeys[i].update_worry()
        if len(tallies) == i:
            tallies.append(len(monkeys[i].inhand))
        else:
            tallies[i] += len(monkeys[i].inhand)
        monkeys[i].throw(monkeys)
        

answer = max(tallies)
tallies.remove(max(tallies))
answer *= max(tallies)

print(answer)
        



    

        
    
            
        
        