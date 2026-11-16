class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 2: Create an array with frequnency index (up to 10n4)
        # Then create hash map
        # Then iterate over the freq array and check for each element whether a hash map entry exists
        hash_map = {}
        for b in nums:
            if b in hash_map:
                hash_map[b] += 1
            else:
                hash_map[b] = 1
        max_freq = max(hash_map.values())
        freq = [[] for _ in range(max_freq + 1)]
        for num, count in hash_map.items():
            freq[count].append(num)
        freq.reverse()
        final = []
        for topk, _ in enumerate(freq):
            for a in freq[topk]:
                final.append(a)
            if len(final) == k:
                return final