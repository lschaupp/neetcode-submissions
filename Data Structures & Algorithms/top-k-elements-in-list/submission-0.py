class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for b in nums:
            if b in hash_map:
                hash_map[b] += 1
            else:
                hash_map[b] = 1
        numbers = sorted(
            hash_map,
            key=lambda x: hash_map[x],
            reverse=True
        )[:k]
        print(numbers)
        return numbers


        