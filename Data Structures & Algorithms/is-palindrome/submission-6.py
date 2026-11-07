class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''
        for l in s:
            if l.isalnum():
                cleaned_string += l.lower()
        return cleaned_string == cleaned_string[::-1]