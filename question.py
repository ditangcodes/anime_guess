def monthly_pay(loan,percentage):
    for x in range(1,4):
        loan = loan - (loan*percentage)
        print(f"Month {x}: \n Amount left to pay: {loan}")

monthly_pay(100000, 0.1)


# You are given a program that takes the length of the array as the 1st input,
#  creates it & then takes the next inputs as elements of the array. 
# Complete the program to go through the array & calculate the sum of the numbers that are multiples of 4.

def length_of_array(array):
    list_of_array = []
    for x in array:
        if x % 4 ==0:
            list_of_array.append(x)
        else:
            pass
    sum_of_arrays = sum(list_of_array)
    print(sum_of_arrays)
length_of_array([1,16,24,8,7,9,55])
    

