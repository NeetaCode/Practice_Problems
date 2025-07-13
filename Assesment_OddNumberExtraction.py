class maxOddString():
    def maxOdd(self, num):
        max_Odd=-1
        value = ""

        for c in num:
            if c.isdigit():
                value += c

            else:
                if value!="":
                    number = int(value)
                    if number%2 == 1 and number > max_Odd:
                        max_Odd = number
                    value = ""

        if value != "":
            number = int(value)
            if number%2 == 1 and number>max_Odd:
                max_Odd = number

        return str(max_Odd) if max_Odd != -1 else ""

sol = maxOddString()
print(sol.maxOdd("mkf43kd1cmk32k1mv123"))  # Output: "123"
print(sol.maxOdd("abcd"))  # Output: ""
