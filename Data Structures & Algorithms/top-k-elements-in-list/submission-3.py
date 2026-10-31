class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else: 
                hash_map[n] = 1
        
        l = list(hash_map.items())
        
        values = set(sorted(list(hash_map.values()), reverse=True)[:k])

        res = []
        for touples in l:
            if touples[1] in values:
                res.append(touples[0])
        return res