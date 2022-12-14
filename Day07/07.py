import os.path

this_folder = os.path.dirname(__file__) + '\\'
input_filename = 'input07.txt'
    # update file name above
input_file_path = this_folder + input_filename

    #prep input in memory
with open(input_file_path, "r") as infile:
    lines = [s.replace('\n', '') for s in infile.readlines()]

# Problem Start ##################################################

# Part 1: Classes and Functions

class File:
    def __init__(self, name, size = None):
        self.name = name
        self.size = size if size is not None else 0

    
    ## example: Folder( name = 'ijkl', 
    ##                  parent = '/abcd/efgh/'
    ##                  files = [file_obj0, file_obj1]
    ##                  subfolders = ['mnop0', 'mnop1']
    ##                  )
    ## <files> contains actual File objects.  <Parent> and <subfolders[]> are just strings,
    ## used for keys in a dictionary (named 'system') that holds Folder objects as its values.
class Folder:
    def __init__(self, name, parent = None, files = None, subfolders = None):
        self.name = name
        self.parent = parent if parent is not None else ''
        self.files = files if files is not None else []
        self.subfolders = subfolders if subfolders is not None else []        
    
    def add(self, item):
        if item.__class__ == File:
            self.files.append(item)
        elif item.__class__ == Folder:
            self.subfolders.append(item.name)
    
        ## used as the key in the dictionary
    def fullpath(self):
        if self.name == '/':
            return '/'
        return self.parent + self.name + '/'    


    ## will communicate  commands from changedir back to build_system function
class cd_obj:
    def __init__(self, isnew = None, fullpath = None, folder = None):
        self.isnew = isnew if isnew is not None else False
        self.newpath = fullpath
        self.folder = folder


    ## takes folder and  command and returns cd_obj(isnew, newpath, folder)
def changedir(folder, command):
    cd = cd_obj()
    if command == '/':
        cd.newpath = '/'
    elif command == '..':
        cd.newpath = folder.parent
    else:
        cd.newpath = folder.fullpath() + command + '/'
        if command not in folder.subfolders:
            cd.isnew = True
        cd.folder = Folder(name = command, parent = folder.fullpath())
    # print(cd.isnew, cd.newpath, cd.folder.name if cd.folder is not None else '0', cd.folder.parent if cd.folder is not None else '0')
    return cd    



# Part 2: More Functions but they're the big important ones ########################

    ## start reading the terminal, and return a completed system (dictionary of folders)
def build_system(lines):
    system = {'/': Folder('/')}
    current_path = '/'
    for line in lines:
        ##print(line)
        args = line.split(' ')
        if args[0:2] == ['$', 'cd']:
            cd = changedir(folder = system[current_path], command = args[2])
            if cd.isnew:
                    ## I'd like to reduce these 2 commands to 1 function
                system[current_path].add(cd.folder)
                system[cd.folder.fullpath()] = cd.folder
            current_path = cd.newpath
        elif args[0:2] == ['$', 'ls']:
            continue
        elif args[0] == 'dir':
                ## I read the prompt wrong and didn't want to rewrite stuff, 
                ## so i'm deciding folders don't exist until I cd into them
            continue
        else:
            newfile = File(name = args[1], size = int(args[0]))
            ##print(newfile)
            system[current_path].add(newfile)
    return system


    ## the whole reason there's a 'system' dict  in the first place is because I couldn't make this function into a method or
    ## property of nested folders.
def get_size(folder, system):
    size = 0
    for file in folder.files:
        size += file.size
    for name in folder.subfolders:
        subpath = folder.fullpath() + name + '/'
        size += get_size(system[subpath], system)
        ## recursion, sucka!
    return size    
     

# Part 3: FEED MARIO ################################################

    ## Yo ass better have some deditated WAM for this one
    
def star1(system):
    ans = 0
    for k, v in system.items():
        n = get_size(v, system)
        if n <= 100000:
            ans += n
            
    return ans


def star2(system):
    used_space = 0
    for k, v in system.items():
        for f in v.files:
            used_space += f.size
    unused_space = 70000000 - used_space
    deletion_needed = 30000000 - unused_space
    ans2 = 0
    for k, v in system.items():
        n = get_size(v, system)
        if ans2 == 0 and n >= deletion_needed:
            ans2 = n
        elif deletion_needed <= n  and n <= ans2:
            ans2 = n        
    return ans2
        

# THE ACTION IS GO ###########################################################

def main():
    system = build_system(lines)
    print('Star 1: ', star1(system))
    print('Star 2: ', star2(system))
    
if __name__ == "__main__":
    main()
    