class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(currentIndex: int):
            if currentIndex == len(nums):
                permutations.append(nums[:])
                return
            j = currentIndex
            aux = 0
            for j in range(currentIndex, len(nums)):
                aux = nums[currentIndex]
                nums[currentIndex] = nums[j]
                nums[j] = aux

                backtrack(currentIndex + 1)

                aux = nums[currentIndex]
                nums[currentIndex] = nums[j]
                nums[j] = aux

        backtrack(0)

        return permutations
