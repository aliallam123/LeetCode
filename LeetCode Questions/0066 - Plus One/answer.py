# my answer
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        list = [1]
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits

            else: 
                digits[i] = 0
                i -= 1

        if i < 0:
            plus_one = list + digits
            return plus_one

        
