while True:
    name = input("Enter your name (or 'stop' to quit): ")
    if name == "stop":
        break
    print("Hello,", name)

#Count to Ten
count=1
while count <= 10:
    print(count)
    count=count+1

#Guess the Secret Number
while True:
    secret_num = int(input("Guess the secret number"))
    if secret_num == 7:
        print("You guessed it right")
        break
    print("Sorry! Try again")

#Countdown Timer Ask the user for a starting number.Count down to 0, printing each number.When done, print "Blast off!".
n=int(input("Enter the starting number")) 
while n>=0:
    print(n)
    n=n-1
print("BLAST OFF!")

#Keep Asking for a Password
while True:
    p = (input("Enter the password"))
    if p == "python":
        print("Access Granted")
        break
    print("Access Denied! Try again")

#Sum Until Zero
total = 0  
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break  
    total = total + number 
print("The total is:", total)

#Even Number Printer
number = 1
while number <= 20:
    if number % 2 == 0: 
        print(number)
    number = number + 1

