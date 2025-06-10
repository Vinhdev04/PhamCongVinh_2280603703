def truy_cap_phan_tu(tuple_data):
    first_e = tuple_data[0]
    last_e = tuple_data[1]
    return first_e, last_e

input_tuple = eval(input("Enter tuple: "))
first,last = truy_cap_phan_tu(input_tuple)
print("First element:", first)
print("Last element:", last)