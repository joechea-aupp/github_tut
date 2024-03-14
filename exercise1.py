'''

Instructions:
-------------

You are given a list of numbers. 

Your task is to duplicate every odd number in the list.

These duplicates should appear at the end of the list. 

Example:

Original list: [1, 3, 5, 2, 8]
Transformed list: [1, 3, 5, 2, 8, 1, 3, 5]  

'''

numbers = [1, 3, 5, 2, 8]

def duplicate_odds(numbers):
    new = []
  
    for i in numbers:
        new.append(i)
        if i % 2 == 1:
            new.append(i)
        
    return new

print(duplicate_odds(numbers))
    

