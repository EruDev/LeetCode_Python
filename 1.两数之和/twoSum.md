## 两数之和

题目描述:

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

	给定 nums = [2, 7, 11, 15], target = 9

	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]

这是我第一次写的, 一开始以为没错, 其实是有错误的, 主要是因为两次遍历有可能跟 target 相同, 返回的 index 就会出错, 而且时间复杂度为O(n^2), 效率太低:

	class Solution:
	    def twoSum(self, nums, target):
	        """
	        :type nums: List[int]
	        :type target: int
	        :rtype: List[int]
	        """
	        if len(nums) == 2:
	            return [0, 1]
	        for i in nums:
	            for j in nums:
	                if i + j == target:
	                    return [nums.index(i), nums.index(j)]


	if __name__ == '__main__':
	    nums = [2, 3, 4]
	    target = 5
	    print(Solution().twoSum(nums, target))
        


后来借鉴了网上大神的代码, 渐渐有点明白了:

	class Solution:
		def twoSum(self, nums, target):
			"""
			:type nums: List[int]
			:type target: int
			:rtype: List[int]
			"""
			dict_temp = dict()
			for index, value in enumerate(nums):
				if targte - value in dict_temp:
					return [dict_temp[target - value], index]
				dict_temp[value] = index

微妙之处就在于 `if targte - value in dict_temp`, 因为 `target = nums[index] + nums[index+1]` 成立的话, 那么 `if targte - value in dict_temp` 肯定是在 `dict_temp` 的键中.