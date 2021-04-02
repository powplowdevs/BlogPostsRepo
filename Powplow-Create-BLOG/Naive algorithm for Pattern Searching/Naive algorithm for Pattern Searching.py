"""
THIS CODE WAS MADE BY POWPLOWDEVS FOR THE POWPLOW-CREATE BLOG YOU CAn FIND IT HERE:
https://powplow-create.blogspot.com/
    
"""

#grab our string of numbers
text = input("Enter your list of numbers: ")
#make ourselfs a string to store the pattern and add the first letter of the text
pat = text[0]
#other variable used for logic
full_pat = ""

for i in range(len(text) - 1):
    #check to see if the letter we are on now is the same as the first letter in our text
    if text[i + 1] != text[0]:
        pat = pat + (text[i + 1]) 
        
    #if the letter is the same
    else:
        #check to see if the next few checters in the text macth out pattern
        if text[i+1:((i+1)*2)] == pat:
            full_pat = full_pat + pat
            break
        #if they dont
        else:
            for j in range(len(text[i:])):
                #add on more from pattern until it equals the next few checters in the text
                if (pat + text[i + 1]) == text[j+1:((j+1)*2)]:
                    print("pattern is:", text[j+1:((j+1)*2)])
                    exit()
  
#check if the pattern is correct        
if full_pat == text[:len(full_pat)]:
    print("pattern is:", str(full_pat))
#if its not say there is no patterns
else:
    print("there is no pattern is this data")


   