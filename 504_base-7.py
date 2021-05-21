# n = num.length
# time = O(n)
# space = O(1)
# done time = 20m


class Solution:

    def convertToBase7(self, num: int) -> str:
        def convert_abs_num_to_base_seven(num: int) -> str:
            MOD = 7
            mods = []

            cur_num = num
            while MOD <= cur_num:
                div, mod = divmod(cur_num, MOD)
                mods.append(str(mod))
                cur_num = div
            mods.append(str(cur_num))
            return ''.join(reversed(mods))


        if num == 0:
            return '0'

        abs_num_with_base_seven_str = convert_abs_num_to_base_seven(abs(num))

        return abs_num_with_base_seven_str if 0 < num else f'-{abs_num_with_base_seven_str}'
