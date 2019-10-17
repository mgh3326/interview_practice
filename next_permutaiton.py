def next_permutations(nums):
    # i찾기
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    # 마지막 순열인 경우 다음순열이 없으므로 False 반환
    if i == 0:
        return False

    # j찾기
    j = len(nums) - 1
    while j > 0 and nums[i - 1] >= nums[j]:
        j -= 1

    # a[i-1]와 a[j]를 바꾸기
    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # 내림차순을 오름차순으로 정렬하기
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return True


input_list = [1, 2, 3, 4]
while True:
    if next_permutations(input_list):
        print(input_list)
    else:
        break