#Get our starting number
number_to_start = int(input("Enter your number: "))

#reverse numbers
def revs(num):
  test_num = 0

  while num>0:
    remainder = num % 10
    test_num = (test_num * 10) + remainder
    num = num//10
 
  return test_num

#Our algorithm
def palindrome_find(number):
    #get the amount we will add and remove from our starting number to get our new number
    number_plus = number
    number_neg = number
    
    while True:
      #add to our amount we will add and remove from our starting number to get our new number
      number_plus = number_plus + 1
      number_neg = number_neg - 1
      
      #check to see if our new number is a palindrome
      if str(number_plus) == str(revs(number_plus)):
        print("The next palindrome is:", number_plus)
        break
      
      elif str(number_neg) == str(revs(number_neg)):
        print("The next palindrome is:", number_neg)
        break

#Get results 
palindrome_find(number_to_start)