class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s = "".join(char for char in s if char.isalnum())
        # n = len(s)
        # if n == 0 or n == 1: #base case 
        #     return True

        # mid = len(s)//2 
        # if n % 2 == 1:
        #     return s[:mid] == s[n-1:mid:-1]
        # else:
        #     return s[:mid] == s[n-1:mid-1:-1]

        #two pointer 
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
        