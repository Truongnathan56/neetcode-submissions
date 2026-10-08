class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        sum = []
        while l < r:
            current = numbers[l] + numbers[r]
            if current < target and l < r:
                l += 1
            elif current > target and r > l:
                r -= 1
            elif current == target:
                sum.append(l + 1)
                sum.append(r + 1)
                return sum
            
        return sum