class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.to_hash_map(s) == self.to_hash_map(t)
    
    def to_hash_map(self, string: str) -> dict:
        hash_map = {}
        for letter in string:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        return hash_map
        