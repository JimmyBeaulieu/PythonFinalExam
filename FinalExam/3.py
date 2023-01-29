# Given a list of non-negative integers nums, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.
# Example 1:
# Input: nums = [10,2]
# Output: "210"
# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# Example 3:
# Input: nums = [1]
# Output: "1"
# Example 4:
# Input: nums = [10]
# Output: "10"

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

nums = [3, 30, 34, 5, 9]
#nums = [10, 2]
#nums = [1]
#nums = [10]

i = 0
newNums = []
while i < len(nums):
    firstNum, secondNum = divmod(nums[i], 10)
    if firstNum == 0:
        newNums.append(secondNum)
    else:
        newNums.append(firstNum)
        newNums.append(secondNum)
    i += 1

sortedNums = sorted(newNums, reverse=True)
i = 0
result = ""
while i < len(sortedNums):
    result += str(sortedNums[i])
    i += 1

print(result)
