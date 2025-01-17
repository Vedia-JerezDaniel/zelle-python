from random import randrange

def mergeMax(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0 , 0
    n1, n2 = len(lst1), len(lst2)
    while i1 < n1 and i2 < n2:
        if lst1[i1] > lst2[i2]:     #top of lst1 is larger
            lst3[i3] = lst1[i1]     #copy it into current spot in lst3
            i1 += 1
        else:               #top of lst2 is larger
            lst3[i3] = lst2[i2]     #copy it into current spot in lst3
            i2 += 1
        i3 += 1

    #Here either lst1 or lst2 is done. One of the following loops will
    #execute to finish up the merge
    #Copy remaining items(if any) from lst1
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 += 1
        i3 += 1
    #Copy remaining items (if any) from lst2
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1

def mergeSort(nums):
    n = len(nums)
    if n > 1:
        #split into two sublists
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        #recursively sort each piece
        mergeSort(nums1)
        mergeSort(nums2)
        #merge the sorted pieces back into original list
        return mergeMax(nums1, nums2, nums)


list = [randrange(1, 13) for _ in range(10)]
ml2 =mergeSort(list)
print(list)
ml2

m = len(list)// 2
nums1, nums2 = list[:m], list[m:]
nums1
ml =mergeMax(nums1, nums2,list)
ml