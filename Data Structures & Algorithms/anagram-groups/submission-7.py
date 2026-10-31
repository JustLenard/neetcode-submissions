class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(s)
            else:
                hash_map[sorted_word] = [s]
        return list(hash_map.values())