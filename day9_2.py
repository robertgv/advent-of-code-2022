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
    
    head_pos = ["0,0"]
    rope = []
    for _ in range(9):
        rope.append(["0,0"])

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
            
            for n in range(1,int(number)+1):
                head_pos.append(f"{current_head_x+(n*x)},{current_head_y+(n*y)}")
                for node in range(len(rope)):
                    previous_node = rope[node-1][len(rope[node-1])-1] if node>0 else head_pos[len(head_pos)-1]
                    curr_node = rope[node][len(rope[node])-1]
                    previoys_node_x, previous_node_y = map(int,(previous_node).split(","))
                    current_node_x, current_node_y = map(int,(curr_node).split(","))
                    diff_x = previoys_node_x-current_node_x
                    diff_y = previous_node_y-current_node_y
                    current_node_x, current_node_y = move_tail(current_node_x, current_node_y, diff_x, diff_y)
                    rope[node].append(f"{current_node_x},{current_node_y}")

    print(f"Total positions: {len(set(rope[8]))}")
    
if __name__ == "__main__":
    main()