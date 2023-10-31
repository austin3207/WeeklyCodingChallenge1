# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def magic_index(arr):
    for i in range(0, len(arr)):
        if i == arr[i]:
            print("Index " + str(i) + " is a Magic number.")
            return
    print("There is no magic number.")


def recursive_multiply(num_1, num_2):
    # Could add a check for which number is smaller to reduce subtractions, but would require an additional method
    if num_2 > 1:
        return recursive_multiply(num_1, num_2-1) + num_1
    else:
        return num_1


def power_set(arr):
    subsets = []
    line = []
    size = len(arr)
    for i in range(1 << size):
        for j in range(size):
            if(i & (1 << j)) != 0:
                line.append(arr[j])
        subsets.append(line)
        line = []
    return subsets


if __name__ == '__main__':
    print("Weekly Coding Challenge")
    print("Find Magic Number")
    array = [1, 0, 2]
    print(array)
    magic_index(array)
    print()
    print("Recursive Multiply")
    print(recursive_multiply(5, 6))
    print()
    print("Subset of set.")
    print(array)
    print()
    subsets = power_set(array)
    for element in subsets:
        print(element)


