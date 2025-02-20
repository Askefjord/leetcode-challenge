def two_sum(nums, target):
    """
    O(n^2)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result = nums[i] + (nums[j])
            if result == target:
                return [i, j]


def two_sum_hard(nums, target):
    """
    O(N)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print(two_sum([2,7,11,15], 9))  # -> [0, 1]
print(two_sum_hard([2, 5, 5, 11], 10)) # -> [1, 2]
