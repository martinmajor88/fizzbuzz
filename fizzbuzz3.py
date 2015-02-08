import sys

for arg in sys.argv[1:]:
  
  x = int(arg) + 1

  if x > 0:

    print "Hokey Dokes! Lets do some Fizzbuzzing to "
    print x

  for n in range (1, x):
    if n%15 == 0:
      print("fizzbuzz")
    elif n%5 == 0:
        print ("buzz")
    elif n%3 == 0:
        print ("fizz")
    else:
      print (n)
  quit()
      
else:
  my_input = raw_input("Enter the highest number you want to Fizz and Buzz to! ")
  print "Hokey Dokes! Lets do some Fizzbuzzing to "
  print (my_input)
  y = int(my_input) + 1

  for n in range (1, y):
    if n%15 == 0:
      print("fizzbuzz")
    elif n%5 == 0:
        print ("buzz")
    elif n%3 == 0:
        print ("fizz")
    else:
      print (n)