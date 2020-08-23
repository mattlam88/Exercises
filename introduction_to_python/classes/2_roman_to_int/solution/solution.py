class py_solution:
    def roman_to_int(self, s):
        roman_val = {"I":1, "V":5, "X":10, "L":50, "C":100, "M":1000}
        number = 0

        for i in range(len(s)):
            if i > 0 and roman_val[s[i]] > roman_val[s[i-1]]:
                number = roman_val[s[i]] - 2 * roman_val[s[i-1]]
            else:
                number += roman_val[s[i]]
        return number
