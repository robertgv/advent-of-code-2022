# Day 8
import string
import math

def main():
    highest_scenic_score=0
    forest = []
    with open('day8.txt') as file:
        for line in file:
            forest.append([x for x in line.strip()])

    for i in range(len(forest)):
        for j in range(len(forest[0])):
            
            current_tree = forest[i][j]
            list_scenic_scores = []
            trees_left = forest[i][:j][::-1]
            trees_right = forest[i][j+1:]
            trees_upper = [row[j] for row in forest[:i]][::-1]
            trees_down = [row[j] for row in forest[i+1:]]

            for trees in [trees_left,trees_right,trees_upper,trees_down]:
                found = False
                count = 0
                while not found and count<len(trees):
                    if trees[count] >= current_tree:
                        found=True
                        list_scenic_scores.append(count+1)
                    else:
                        count+=1
                if count==len(trees):
                    list_scenic_scores.append(len(trees))

            scenic_score = math.prod(list_scenic_scores)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    print(f"Highest scenic score: {highest_scenic_score}")
    
if __name__ == "__main__":
    main()