# compare the current measurement with the previous one
INPUT_TEXT_FILE = "advent_of_code_one.txt"

# reads text from the file into a string
with open(INPUT_TEXT_FILE, "r") as f:
    depths = f.readlines()

    count = 0
    # i will equal the current item, so we must start i with 1
    for i in range(1, len(depths)):
        # Compare previous with the current, note: use "i - 1" to represent "the next item"
        if int(depths[i - 1]) < int(depths[i]):
            #   add the values to the counter variable (count)
            count += 1

    print(count)
