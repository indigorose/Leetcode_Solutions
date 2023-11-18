''' For a number of steps given (n) return the number of steps required to get to 0
when you either divide by two when n is even or subtract one when odd.'''

'''
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
                count += 1
            else:
                num -=1
                count +=1
        return count
'''

''' Explanation - There are two things we need to observe, the number of steps required
    to get to zero and what is happening at each turn. First we initialise a count variable to help keep track of each "turn" and return our answer. Secondly a while loop will help us go through each turn in the range of n. In this case the conditional to stop the loop will be when n == 0. Hence "while num !=0" our loop will continue. As we take a turn we use a further boolean conditional to check for the even and taking action (num/2) when true or moving on to subtract 1 when odd. Each turn will also add to our count answer. When the loop condition is no longer satisfied, we break the loop and return our count.'''