

def read_input():
    list1, list2 = [], []
    input_file = open('practice_input.txt', 'r')
    while True:
        content=input_file.readline().split()
        if not content:
            break
        list1.append(int(content[0]))
        list2.append(int(content[1]))
    input_file.close()
    return list1, list2


def calculate_differences(list1, list2):
    total_diff = 0
    while len(list1) >= 1:
        min1 = min(list1)
        min2 = min(list2)
        total_diff += abs(min1 - min2)
        list1.remove(min1)
        list2.remove(min2)
    return total_diff


if __name__ == "__main__":
    list1, list2 = read_input()
    total_difference = calculate_differences(list1, list2)
    print(total_difference)