import re

def read_input():
    input_file = open('input.txt', 'r')
    content = input_file.read()
    return content


def process_input(input):
    multiplications = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    sum = 0
    for multiplication in multiplications:
        values = re.findall(r"\d+", multiplication)
        sum += int(values[0]) * int(values[1])
    return sum
    

if __name__ == "__main__":
    input = read_input()
    output = process_input(input)
    print(f"{output = }")