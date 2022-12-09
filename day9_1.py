# Day 4
import string

def main():

    def move_tail(current_tail_x, current_tail_y, diff_x, diff_y):
        if (abs(diff_x)==1 and (abs(diff_y)==2)) or (abs(diff_x)==2 and (abs(diff_y)==1)):
            current_tail_x += diff_x//abs(diff_x)
            current_tail_y += diff_y//abs(diff_y)
        else:
            if (abs(diff_x)>1):
                if diff_x>1:
                    current_tail_x += 1
                elif diff_x<-1:
                    current_tail_x -= 1
            if (abs(diff_y)>1):
                if diff_y>1:
                    current_tail_y += 1
                elif diff_y<-1:
                    current_tail_y -= 1
        return current_tail_x, current_tail_y
    
    head_pos=["0,0"]
    tail_pos=["0,0"]
    with open('day9.txt') as file:
        for line in file:
            move, number = line.strip().split(" ")
            current_head_x, current_head_y = map(int,(head_pos[len(head_pos)-1]).split(","))

            if move == "L":
                x = -1
                y = 0                    
            elif move == "R":
                x = 1
                y = 0
            elif move == "U":
                x = 0
                y = 1
            elif move == "D":
                x = 0
                y = -1
            else:
                raise ValueError("Move not detected.")
            
            for _ in range(1,int(number)+1):
                head_pos.append(f"{current_head_x+(1*x)},{current_head_y+(1*y)}")
                current_head_x, current_head_y = map(int,(head_pos[len(head_pos)-1]).split(","))
                current_tail_x, current_tail_y = map(int,(tail_pos[len(tail_pos)-1]).split(","))
                diff_x = current_head_x-current_tail_x
                diff_y = current_head_y-current_tail_y
                current_tail_x, current_tail_y = move_tail(current_tail_x, current_tail_y, diff_x, diff_y)
                tail_pos.append(f"{current_tail_x},{current_tail_y}")

    print(f"Total positions: {len(set(tail_pos))}")
    
if __name__ == "__main__":
    main()