# n = bits.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        one_or_two_discriminate_idx = 0
        while one_or_two_discriminate_idx < len(bits):
            is_one_bit_char = False
            if bits[one_or_two_discriminate_idx] == 1:
                one_or_two_discriminate_idx += 2
            else:
                one_or_two_discriminate_idx += 1
                is_one_bit_char = True
        return is_one_bit_char
