class Solution:
    #AAABBAB k = 2
    #AAABBBCBB k = 1
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        left = 0
        max_length = 0
        for end in range(len(s)):
            freq_map[s[end]] += 1
            max_freq = max(freq_map.values())
            if (end - left + 1) - max_freq > k:
                max_length = max(max_length, end - left)
                freq_map[s[left]] -=  1
                left += 1
        return max(max_length, end - left + 1)

                
        # for ch in s:
        #     freq_map[ch] += 1
        
        # most_freq_ch = max(freq_map, key=freq_map.get)
        # max_length = 0
        # curr_length = 0
        # num_replacements = 0

        # for i in range(len(s)):
        #     if s[i] == most_freq_ch:
        #         max_length += 1
        #         continue
        #     else:
        #         if num_replacements < k:
        #             curr_length += 1
        #             num_replacements += 1
        #         else:
        #             max_length = max(max_length, curr_length)
        #             num_replacements = 0
                    
        # return max(max_length, freq_map[most_freq_ch] - max_length)
                

                

        