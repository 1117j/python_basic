""" Use the Python print function to calculate how many number-based 
passcodes can be formed with 10 numerals (0 through 9).  
Here’s a hint to help you: When each digit of a passcode is 
independent of the others, the total number of combinations is 
imply the number of possibilities for each digit raised to the
 power of the length of the passcode. So, for a 1-numeral passcode, 
 there would be 10 possibilities; one for every numeral from 0 to 9.  
 For a 2-numeral passcode, each numeral is independent of the other, 
 so there would be 10 times 10 possibilities. Using this information,
 print the amount of possible passwords that can be formed with 3 numerals. 
 Note:Your result should be in the number format, not a sentence.
"""

num = 10
pw_length = 3 
possible_password = num ** pw_length
print(possible_password)