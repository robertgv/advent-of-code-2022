# Day 2

# -- opponent hands --
    # A for Rock
    # B for Paper
    # C for Scissors

# -- My hands --
    # X for Rock
    # Y for Paper
    # Z for Scissors

def main():
    total=0
    win_results=set(("C X","A Y","B Z"))
    draw_results=set(("A X","B Y","C Z"))
    hand_points=dict({"X":1,"Y":2,"Z":3})
    with open('day2.txt') as file:
        for line in file:
            me = line.strip().split(" ")[1]
            if line.strip() in win_results:
                total+=6
            elif line.strip() in draw_results:
                total+=3
            total+=hand_points[me]
            
    print(f"Total points: {total}")
    
if __name__ == "__main__":
    main()