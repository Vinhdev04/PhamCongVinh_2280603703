def reverseList(lst):
    return lst[::-1]

input_list = input("Enter a list number: ")
numbers = list(map(int, input_list.split(',')))

reversed_list = reverseList(numbers)
print("Reversed list:", reversed_list)