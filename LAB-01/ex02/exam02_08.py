def devide_by_5(num_binary):
    num_decimal = int(num_binary, 2)
    if num_decimal % 5 == 0:
        return True
    else:   
        return False
    
str_binary = input("Enter a binary number: ")
num_binary_list = str_binary.split(',')
devide_by_5 = [so for so in num_binary_list if devide_by_5(so)]

if len(devide_by_5) > 0:
    result = ','.join(devide_by_5)
    print("Output: ", result)
else:
    print("No output")