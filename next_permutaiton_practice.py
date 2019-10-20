def next_permutations(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i == 0:
        return False
    j = len(nums) - 1
    while j > 0 and nums[i - 1] >= nums[j]:
        j -= 1
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    # reverse
    j = len(nums) - 1
    while True:
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return True


input_list = [0, 0, 0, 1]
while True:
    if next_permutations(input_list):
        print(input_list)
    else:
        break
