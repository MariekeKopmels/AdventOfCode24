

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


def calculate_similarity_score(list1, list2):
    similarity_score = 0
    for item in list1:
        similarity_score += item * list2.count(item)
    return similarity_score


if __name__ == "__main__":
    list1, list2 = read_input()
    similarity_score = calculate_similarity_score(list1, list2)
    print(similarity_score)