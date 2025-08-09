#Print numbers from 1 to 10
for i in range(11):
    print(i)

#Print even numbers from 0 to 20
for i in range(21):
    if i%2==0:
        print(i)

#Print the square of numbers from 0 to n
n=int(input())
for i in range(n):
    print(i*i)

#Print multiplication table of a number
n=int(input())
for i in range(11):
    print(f"{n}*{i}={n*i}") #use of f-string

#Sum of numbers from 1 to n
n=int(input())
total=0
for i in range(i,n+1):
    total+=i
    print("Sum from 1 to", n, "is:", total)