def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Enter list: ")
numbers =list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("list: ",numbers)
print("Tuple in list: ",my_tuple)