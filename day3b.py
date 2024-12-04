import re

def read_input():
    input_file = open('input.txt', 'r')
    content = input_file.read()
    return content


def process_input(input):
    remaining_string = input

    substrings = re.split("(mul\([0-9]{1,3},[0-9]{1,3}\))", input)
    sum = 0
    enabled = 1
    for substring in substrings:
        if enabled == 1 and re.match("(mul\([0-9]{1,3},[0-9]{1,3}\))", substring):
            values = re.findall(r"\d+", substring)
            sum += int(values[0]) * int(values[1])
        else:
            enabled = update_enabled(substring, enabled)

    return sum


def update_enabled(substring, enabled):
    do_location = substring.find("do()")
    dont_location = substring.find("don't()")
    if do_location != -1:
        if dont_location != -1:
            return 1 if do_location > dont_location else -1
        else: 
            return 1
    elif dont_location != -1:
        return -1

    return enabled
    

if __name__ == "__main__":
    input = read_input()
    output = process_input(input)
    print(f"{output = }")