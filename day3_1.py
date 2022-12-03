# Day 3
import string

list_letters = {**dict(zip(string.ascii_lowercase,range(1, 27))),**dict(zip(string.ascii_uppercase,range(27, 53)))}

def main():
    total=0
    with open('day3.txt') as file:
        for line in file:
            line=line.strip()
            pos=len(line)//2
            letter=list(set(line[:pos]).intersection(line[pos:]))[0]
            total+=list_letters[letter]
            
    print(f"Total points: {total}")
    
if __name__ == "__main__":
    main()