# Day 6
import string

def main():
    with open('day6.txt') as file:
        line = file.readline()
        for char in range(len(line)-14):
            sub_line = line[char:char+14]
            if len(set(sub_line)) == 14:
                print(f"Result : {char+14}")
                exit()
    
if __name__ == "__main__":
    main()