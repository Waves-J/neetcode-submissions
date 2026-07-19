class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # We pass a starting index 'i' to track which position we are filling
        def backtrack(i):
            # Base Case: If our starting index has reached the end of the array,
            # it means we have successfully locked in a number for every position.
            if i == len(nums):
                # We append a copy of the CURRENT STATE of the nums array.
                res.append(nums[:])
                return
            
            # We iterate through all numbers from our current index 'i' to the end.
            for j in range(i, len(nums)):
                
                # DECISION: We swap the number at index 'j' into our current position 'i'.
                # This "locks in" a new number at position 'i'.
                nums[i], nums[j] = nums[j], nums[i]
                
                # We recursively explore all permutations for the REMAINING positions (i + 1)
                backtrack(i + 1)
                
                # CLEANUP (Backtracking): We must undo the swap!
                # This restores the array to its original state so the next iteration 
                # of the loop can try swapping a different number into position 'i'.
                nums[i], nums[j] = nums[j], nums[i]
                
        # Start the recursion at the very first index (0)
        backtrack(0)
        return res