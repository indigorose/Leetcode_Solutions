# for a 2d array of accounts, return the wealthiest(max value) account.

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         return max([sum(i) for i in accounts])

''' Explanation
For this example we are given customer with three bank accounts stored in a single array and held in array of customers, hence the 2D array. Given that we are returning the wealthiest customer rather than the wealthiest bank, we can use our knowledge of for loops and the built in sum function. As we go through each array (i) we are returning a sum that can be stored in a new array (results). Furthermore with our results we can use a built in function of python (max) to return the largest number and answer. 
Refactoring this to a ternary operator allows us to combine these inbuilt functions.
'''