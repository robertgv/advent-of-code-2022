# Day 8
import string

def main():
    total_visible_trees=0
    forest = []
    with open('day8.txt') as file:
        for line in file:
            forest.append([x for x in line.strip()])

    total_visible_trees += (len(forest[0])*2)+(len(forest)*2)-4

    for i in range(1,len(forest)-1):
        for j in range(1,len(forest[0])-1):
            
            # Check the left and right side
            max_left_side = max(forest[i][:j])
            max_right_side = max(forest[i][j+1:])

            # Check the upper and down side
            max_upper_side = max([row[j] for row in forest[:i]])
            max_down_side = max([row[j] for row in forest[i+1:]])
            
            if (forest[i][j] > max_down_side) or \
                (forest[i][j] > max_upper_side) or \
                (forest[i][j] > max_right_side) or \
                (forest[i][j] > max_left_side):
                total_visible_trees+=1

    print(f"Total visible trees: {total_visible_trees}")
    
if __name__ == "__main__":
    main()