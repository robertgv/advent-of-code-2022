# Day 4
import string

def main():
    total=0
    with open('day4.txt') as file:
        for line in file:
            elf_1,elf_2=line.strip().split(",")
            elf_1_0, elf_1_1=[int(x) for x in elf_1.split("-")]
            elf_2_0, elf_2_1=[int(x) for x in elf_2.split("-")]
            if ((elf_1_0 >= elf_2_0) and (elf_1_1 <= elf_2_1)) or ((elf_2_0 >= elf_1_0) and (elf_2_1 <= elf_1_1)):
                total+=1

    print(f"Total points: {total}")
    
if __name__ == "__main__":
    main()