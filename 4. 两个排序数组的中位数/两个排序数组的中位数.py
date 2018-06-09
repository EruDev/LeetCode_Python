# coding: utf-8

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

示例 1:
nums1 = [1, 3]
nums2 = [2]

中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
"""
def findMedianSortedArrays(nums1, nums2):
	"""
	简单粗暴, 就是效率太低
	"""
	nums3 = sorted(nums1 + nums2)
	mid = 0
	mid_index2 = 0
	mid_index = 0
	if len(nums3) % 2 == 1:
		mid_index = len(nums3) // 2
		mid = nums3[mid_index]
	else:
		mid_index = int(len(nums3) / 2)
		mid_index2 = mid_index - 1
		mid = (nums3[mid_index] + nums3[mid_index2]) / 2
	return mid

# nums1 = [1, 3]
# nums2 = [2]
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
