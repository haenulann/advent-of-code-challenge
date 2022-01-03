# count the number of times the sum of measurements
# in this sliding window increases from the previous sum

#   use same code as dayOne.py

INPUT_TEXT_FILE = "advent_of_code_one.txt"

# reads integers from text file
with open(INPUT_TEXT_FILE, "r") as f:
    depths = [int(line) for line in f]

    count = 0
    # i will equal the current item, so we must start i with 3
    for i in range(3, len(depths)):
        # math
        left = depths[i - 3] + depths[i - 2] + depths[i - 1]
        right = depths[i - 2] + depths[i - 1] + depths[i]
        if left < right:
            #   add the values to the counter variable (count)
            count += 1

    print(count)
