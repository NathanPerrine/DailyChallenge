def merge_sort(nums1, m, nums2, n):
    l, r, = 0, 0
    while n > 0:
        n1 = nums1[l]
        n2 = nums2[r]

        if n1 == n2: 
            nums1.insert(l+1, n2)
            nums2.pop(0)
            l += 2
            n -= 1
        if n1 < n2:
            if n1 == 0:
                nums1[l] = n2
                nums2.pop(0)
                l += 1
                n -= 1
                continue
            elif nums1[l+1] < n2:
                l += 1
                continue
            else:
                nums1.insert(l+1, n2)
                nums2.pop(0)
                l += 2
                n -= 1
        else: 
            l += 1

    while nums1[-1] == 0:
        nums1.pop()

    return nums1






nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge_sort(nums1, m, nums2, n))
print([1,2,2,3,5,6])
print("======")

nums1 = [1]
m = 1
nums2 = []
n = 0
print(merge_sort(nums1, m, nums2, n))
print([1])
print("=====")


nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge_sort(nums1, m, nums2, n))
print([1])