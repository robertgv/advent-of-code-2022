# Day 3
import string

list_letters = {**dict(zip(string.ascii_lowercase,range(1, 27))),**dict(zip(string.ascii_uppercase,range(27, 53)))}

def main():
    total=0
    with open('day3.txt') as file:
        lines = file.readlines()
        count = 0
        while count<len(lines):
            elve1 = lines[count].strip()
            elve2 = lines[count+1].strip()
            elve3 = lines[count+2].strip()
            letter=list((set(elve1).intersection(elve2)).intersection(elve3))[0]
            total+=list_letters[letter]
            count+=3
            
    print(f"Total points: {total}")
    
if __name__ == "__main__":
    main()