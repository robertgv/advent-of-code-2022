# Day 1

def main():
    elfs = []
    with open('day1.txt') as file:
        line = file.readline()        
        total = 0
        while line:
            if line == "\n":
                elfs.append(total)
                total=0
            else:
                total+=int(line)
            line = file.readline()
    print(f"Max: {max(elfs)}")
    
if __name__ == "__main__":
    main()