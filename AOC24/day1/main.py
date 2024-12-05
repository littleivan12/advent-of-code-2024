from collections import Counter


def part1(s):
    
    # Setting up arrays
    ans = 0 
    left = []
    right = []

    # Convert the strings from text file to ints.
    # Placeing the left and right column numbers in the apporiate array.
    for l in s.split("\n"):
        l = [int(x) for x in l.split()]  # Convert each line into integers
        left.append(l[0])  # First number goes to `left`
        right.append(l[1])  # Second number goes to `right`
    ## Sorting array
    left.sort()
    right.sort()
    
    # Calculating the distance
    for i in range(len(left)):
        ans += abs((left[i] - right[i]))
    
    print("Answer for Part 1",ans)
    
def part2(s):

    left = []
    right = []

    # Convert the strings from text file to ints.
    # Placeing the left and right column numbers in the apporiate array.
   
    for l in s.split("\n"):
        l = [int(x) for x in l.split()]  
        left.append(l[0])  
        right.append(l[1])  

    # Create a Counter for `right` to count occurrences of each number
    right_counter = Counter(right)

    similarity_score = 0

    # Calculate the similarity score
    for l in left:
        similarity_score += l * right_counter[l]  # Multiply number by its frequency in `right`

    print("Answer for part 2:",similarity_score)




with open('/Users/ivancandelero/Desktop/AOC24/day1/input.txt') as file:
        s = file.read().strip()
part1(s)
part2(s) 