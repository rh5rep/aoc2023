import os.path

filename = "day1input.txt"

nums_in_line = []
first_last = 0
sum = 0

with open(filename) as f:

    content = f.read().splitlines()

    for line in content:
        for char in line:
            if char.isnumeric():
                nums_in_line.append(char)

        first_last = int(str(nums_in_line[0]) + str(nums_in_line[-1]))
        nums_in_line = []
        sum += first_last

    print(sum)