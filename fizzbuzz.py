#Create a program that will run through the integers 1 to 25.
#If the number is a multiple of 3, print "Fizz"
#If the number is a multiple of 5, print "Buzz"
#If the number is a multiple of 3 and 5 print "FizzBuzz"
#If the number is not any of the stated multiples, print the number.
#Each output is on it's own line
#Also include in your repo a .drawio file that flowcharts out the logic

#Here is a section of sample output:
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz

for num in range(1, 26):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)