class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''

        for ch in s:
            if ch.isalnum():
                cleaned_string += ch.lower()
        return cleaned_string == cleaned_string[::-1]