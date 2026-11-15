class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Create a dict of letters and its' count of s2
        # 2. Loop overt the strings of s1 and check the dict
        # if letter present in dict substract 1 from the value (up to 0)
        # if we letter not present or reached 0 return false
        # reuturn true

        if len(s1) > len(s2):
            return False

        def to_dict(substring: str) -> dict:
            dict_with_letters = defaultdict(int)

            for letter in substring:
                dict_with_letters[letter] += 1
            return dict_with_letters

        s1_dict = to_dict(s1)

        i , j = 0 , len(s1)

        current_s2_substring= s2[i: j]
        current_s2_dict = to_dict(current_s2_substring)

        if s1_dict == current_s2_dict:
            return True


        while j < len(s2):
            if current_s2_dict[s2[i]] == 1:
                del current_s2_dict[s2[i]]
            else:
                current_s2_dict[s2[i]] -= 1

            i += 1
            j += 1
            print(j)
            if s2[j - 1] in current_s2_dict:
                current_s2_dict[s2[j - 1]] += 1
            else:
                current_s2_dict[s2[j - 1]] = 1


            if s1_dict == current_s2_dict:
                return True

        return False


            