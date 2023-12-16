import os
with open(os.path.dirname(__file__) + "/input.txt", 'r') as f:
    lines = f.readlines()

num_spellings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def text_to_num(line: str):
    for num_spelling in num_spellings:
        while num_spelling in line:
            for i in range(len(line)):
                for j in range(len(line)):
                    if i < j:
                        curr = ''.join(line[i:j])
                        if curr == num_spelling:
                            line = list(line)
                            line[i+1] = num_spellings[num_spelling]
                            line = ''.join(line)
    return line


calibration_values: list[int] = []
for line in lines:
    first_num = None
    last_num = None
    line = text_to_num(line)
    for char in line:
        if char.isnumeric():
            if not first_num:
                first_num = char
            last_num = char
    calibration_values.append(int(first_num + last_num))
print(sum(calibration_values))
