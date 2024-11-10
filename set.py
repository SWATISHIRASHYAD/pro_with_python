class Solution:
    def firstMissingPositive(self, nums) -> int:
        set(nums)
        print(nums)
        nums.sort()
        print(nums)
        if 1 not in nums:
            return 1
        index=nums.index(1)
        while index < len(nums)-1:
            if nums[index+1]!=nums[index]+1:
                return nums[index]+1
            index+=1
        return nums[index]+1
obj=Solution()
obj.firstMissingPositive([1,1,0,2,2])
