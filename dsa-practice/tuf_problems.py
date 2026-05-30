
def removeDuplicates(nums : list[int]) -> int:
    if not nums:
        return 0;

    cursor = 0;

    for i in range(1, len(nums)):
        if nums[i] != nums[cursor]:
            cursor += 1
            nums[cursor] = nums[i]

    return cursor + 1


# uniqueElements = removeDuplicates([1, 1, 2, 2, 3, 3])
# print(uniqueElements)

def rotateOneLeft(nums : list[int]) -> None:
    if not nums:
        return;

    firstEl = nums[0];
    for i in range(0, len(nums) - 1):
        nums[i] = nums[i+1];

    nums[len(nums) - 1] = firstEl;

arr = [1,2,3,4,5];
rotateOneLeft(arr);
print(arr);

