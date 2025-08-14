#Count Positive Numbers
#Write a function that takes a list of numbers and prints how many numbers are positive.
def count_positive(numbers):
    count = 0  # To count how many numbers are positive
    for num in numbers:
        if num > 0:
            count += 1
    print(count)
count_positive([-1, 0, 2, 5, -3])

#Multiplication Table
#Write a function that takes a number n and prints its multiplication table up to 10.
def multiplication_table(n=3):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    # Call without arguments → prints table for 3
multiplication_table()
    # Call with arguments → prints table for any number
multiplication_table(5)

#Sum of Even Numbers
#Write a function that takes a list and returns the sum of all even numbers.
def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
print(sum_even([1, 2, 4, 3, 7, 8, 10]))

#Check Prime Number
#Write a function that checks if a number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True
print(is_prime(7))  
print(is_prime(10))  

#Reverse a String
#Write a function that reverses a given string without using [::-1].
def reverse_string(s):
    reversed_str = ""           
    for char in s:               
        reversed_str = char + reversed_str  
    return reversed_str
print(reverse_string("hello")) 


