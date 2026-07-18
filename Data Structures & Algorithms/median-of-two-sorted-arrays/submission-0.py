class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        mergedlist = []
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                mergedlist.append(nums1[i])
                i += 1
            else:
                mergedlist.append(nums2[j])
                j += 1
        while i < l1:
            mergedlist.append(nums1[i])
            i += 1
        while j < l2:
            mergedlist.append(nums2[j])
            j += 1
        n = len(mergedlist)
        if n % 2 == 0:
            return (mergedlist[n // 2] + mergedlist[n // 2 - 1]) / 2
        else:
            return mergedlist[n // 2]

        


            
        
            
