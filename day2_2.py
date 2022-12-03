# Day 2

# -- opponent hands --
    # A for Rock
    # B for Paper
    # C for Scissors

# -- My hands --
    # X means you need to lose
    # Y means you need to end the round in a draw
    # Z means you need to win

def main():
    total=0
    win_map=dict({"C":"X","A":"Y","B":"Z"})
    draw_map=dict({"A":"X","B":"Y","C":"Z"})
    lose_map=dict({"A":"Z","B":"X","C":"Y"})
    hand_points=dict({"X":1,"Y":2,"Z":3})
    with open('day2.txt') as file:
        for line in file:
            opponent, me = line.strip().split(" ")
            if me == "X":
                total+=hand_points[lose_map[opponent]]
            elif me == "Y":
                total+=hand_points[draw_map[opponent]]+3
            elif me == "Z":
                total+=hand_points[win_map[opponent]]+6
            
    print(f"Total points: {total}")
    
if __name__ == "__main__":
    main()