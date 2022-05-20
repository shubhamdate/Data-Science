#from numpy import array

def sort(nums):
    
    for i in range(0, len(nums)-1):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
nums = input("Enter the number in Array :").split()
nums = [int(x) for x in nums ]
# nums = [4, 43, 43, 33, 24, 32, 23]
sort(nums)
print("Sortd array using selection sort is :",nums)


arr = input("Enter ")