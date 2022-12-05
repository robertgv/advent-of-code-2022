# Day 5
import string

def main():
    result = ""
    n_stacks = 0
    stacks = []
    with open('day5.txt') as file:
        
        for line in file:
            if (line[0] == "[") or (line[:3] == "   "):
                if not n_stacks:
                    n_stacks = len(line)//4
                    for _ in range(n_stacks):
                        stacks.append([])
                count=1
                for stack in range(n_stacks):
                    value = line[count]
                    if (value != " ") and (not value.isnumeric()):
                        stacks[stack].append(value)
                    count+=4
            elif line[:3] == " 1 ":
                for stack in range(n_stacks):
                    stacks[stack] = stacks[stack][::-1]
            elif line[0] == "m":
                line = line.replace("move ","").replace(" from "," ").replace(" to "," ").strip()
                move, source, dest = map(int, line.split(" "))
                for _ in range(move):
                    stacks[dest-1].append(stacks[source-1].pop())

    for stack in stacks:
        result += stack.pop()

    print(f"Total points: {result}")
    
if __name__ == "__main__":
    main()