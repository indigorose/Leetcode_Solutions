''' Return a string based array length of "n" which highlights numbers that are 
divisible by 3 and 5 as "FizzBuzz, numbers divisible by 3 as "Fizz" and numbers divisible by 5 as "Buzz". '''


'''class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif (i % 3 == 0):
                result.append("Fizz")
            elif (i % 5 == 0):
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        
'''

''' Explanation
    With the use of for loops, we are going to create a range of 1 to the length of n+1, n being any number
    between 1 and 10 to the power of 4(aka 10,000). We extend by n+1 as ranged for loops are
    based on counting the index rather than the number, hence 0 = index 1. 
    As we check each number in the position (i), we check the three options of division, using the modulo operator which tests for any remainders when a number is divided
    (true values will not return a remainder) and append a true result 
    to our results array. Those that return false are added as their string. 
    Once complete we return the result as our answer. 
'''