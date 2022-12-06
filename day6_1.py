# Day 6
import string

def main():
    with open('day6.txt') as file:
        line = file.readline()
        for char in range(len(line)-4):
            sub_line = line[char:char+4]
            if len(set(sub_line)) == 4:
                print(f"Result : {char+4}")
                exit()
    
if __name__ == "__main__":
    main()