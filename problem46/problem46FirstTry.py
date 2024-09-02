class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        aux = 1
        for i in range(len(nums)):
            permutations.append(nums[:])
            for j in range(1,len(nums)-1):
                aux = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = aux
                permutations.append(nums[:])
            nums[-1] = nums[0]
            nums[0] = aux
        print(permutations)
        return permutations
