
nums = [1, 7, 7, 7,7,7,2,3, 3]

def stretch(nums):
    prev = nums[0]
    longest = 1
    maxLen = 0

    for i in range(1, len(nums)):
        if nums[i] == prev:
            longest += 1
            maxLen = max(maxLen, longest)
        else:
            longest = 1
            prev = nums[i]


    return maxLen

print(stretch(nums))