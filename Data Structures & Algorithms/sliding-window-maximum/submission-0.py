class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from the window
            if l > q[0]:
                q.popleft()
            
            # Make sure window is at least size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        
        return output

        