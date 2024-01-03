"""
THIS CODE WAS MADE BY POWPLOWDEVS FOR THE POWPLOW-CREATE BLOG YOU CAn FIND IT HERE:
https://powplow-create.blogspot.com/
    
"""

#This list will store all our prime numbers
nums = []

#we start all for loop
#to find all prime numbers for 1 to 100 
for j in range(100):
    
    #for each number we check if is divisibale by any number from 1 to 10
    for i in range(1,10):
        #get our number divided by our second number
        num = j / i 
        #check if its not 1 and not the same as our first number
        if i != j and i != 1:
            #check if its a whole Number
            #if so then end and move on to the next number
            if num.is_integer():
                break
            #if not
            else:
                #make sure that we have check all the numbers in the 1 to 10 list
                if i == 9:
                    #make sure we dont allread have the number in the list
                    if j not in nums:
                        #add the number
                        nums.append(j) 
#show the results 
print(nums)