#The Collatz sequence

#This function does one operation or another based in if the number is even or odd
def collatz(number):
    if even(number):
        return number // 2
    else: #Odd number
        return 3 * number + 1

#This function verifies if the number is even or odd
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#collatz() is exectuted and expects an input from the user,
#it will stop when the return value of collatz() is 1
num = 0
while collatz(num) != 1:
    num =int(input())
    collatz(num)
    print(collatz(num))
