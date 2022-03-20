#Maria Eden Peralta
#March 20, 2022
#M9 Lab Activity



#Problem 1: Write an infinite loop that prints “Infinite”. An infinite loop never ends.
#The condition is always true.

while True:
    print("Infinite")


#Problem 2: Using a while loop, create a list called L that contains the numbers 0 to 10. On each iteration, the loop should append the current value of a counter variable to the list and then increase the counter by 1.
#The while loop should stop once the counter variable is greater than 10.

L = []
i=0
while i<=10:
    L.append(i)
    i=i+1
print(L)

#Problem 3: Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together.
#Continue asking for a number until the sum of the list of numbers is greater than 100.

List = []
i=100
while True:
      n = input('enter the number:')
      List.append(n)
      choice = input("want to exit? press yes, otherwise press any number")
      if choice == "yes":
            break
      
print("list is:", 100)


#Problem 4: Create a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
#Confirm the list results using a print statement.


counter = 0
tens=[]
while(counter<=50):
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print(tens)

