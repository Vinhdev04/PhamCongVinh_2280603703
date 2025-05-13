def sumEven(lst):
    sum= 0
    for num in lst:
        if num%2 ==0:
            sum+=num
    return sum

input_lst = input("Enter list numbers separated by space: ")
numbers = list(map(int, input_lst.split(',')))

sum_of_evens = sumEven(numbers)
print("Sum of even numbers in the list:", sum_of_evens)