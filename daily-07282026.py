class Solution:
    def smallestPalindrome(self, s: str) -> str:

        # Edge case 1: Length of s is less than 2
        if len(s) < 2:
            return s

        # frequency map
        freq_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0
                    ]

        # 97 is a lowercase 'a'. Substract 97 so, 97-97 = 0 index and goes to a (a is 1st char)
        for character in s:
            ascii_val = ord(character)
            index = ascii_val - 97
            freq_arr[index] += 1

        odd_count = 0
        center_char = ""
        
        for i in range(0, 26):
            if freq_arr[i] % 2 != 0:
                odd_count += 1
                center_char = chr(i + 97)
        
        if (len(s) % 2 == 0 and odd_count != 0) or (len(s) % 2 != 0 and odd_count != 1):
            return ""

        # left half of the string
        left_half = ""
        for i in range(0, 26):
            half_count = freq_arr[i] // 2
            char = chr(i + 97)
            left_half += char * half_count

        # right half of the string
        right_half = ""
        for j in range(len(left_half) - 1, -1, -1):
            right_half = right_half + left_half[j]

        if len(s) % 2 != 0:
            return left_half + center_char + right_half
        else: 
            return left_half + right_half
            
        
