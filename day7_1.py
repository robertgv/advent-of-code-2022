# Day 7
from anytree import Node, RenderTree

def main():

    root = Node("root")
    current_path = [root]
    total_size = 0
    folders_size = dict()
    total_folder_size = dict()
    after_read_folder = False
    total_sum = 0 # Of folder below 100000 size
    
    def total_size_folder(node):
        size = folders_size[node]
        if len(node.children) > 0:
            for child in node.children:
                size += total_size_folder(child)
        return(size)

    with open('day7.txt') as file:
        for line in file:
            current_folder = current_path[len(current_path)-1]
            if line.startswith("$ "): # Shell command (cd or ls)
                if after_read_folder:
                    folders_size[current_folder] = total_size
                    after_read_folder = False
                total_size = 0
                if line.startswith("$ ls"):
                    after_read_folder = True
                elif line.startswith("$ cd"):
                    order = line.replace("$ cd ","").strip()
                    if order == "/":
                        current_path = [root]
                    elif order == "..":
                        current_path.pop()
                    elif order != ".":
                        new_node = Node(order, parent=current_folder)
                        current_path.append(new_node)
                else:
                    raise ValueError(f"Shell command not specified: {line}")
            else: # List current path
                if not line.startswith("dir "):
                    size = line.split(" ")[0]
                    total_size += int(size)
    
    # In case last command was "ls"
    if after_read_folder:
        folders_size[current_folder] = total_size

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
        node.name
    
    for node in folders_size.keys():
        total_size = total_size_folder(node)
        if total_size <= 100000:
            total_sum += total_size
        total_folder_size[node] = total_size
    
    print(folders_size)
    print(total_folder_size)
    print(total_sum)

if __name__ == "__main__":
    main()