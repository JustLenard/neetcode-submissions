class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''

        for ch in s:
            if ch.isalnum():
                cleaned_string += ch.lower()
        print(cleaned_string)
        print(cleaned_string[::-1])
        return cleaned_string == cleaned_string[::-1]