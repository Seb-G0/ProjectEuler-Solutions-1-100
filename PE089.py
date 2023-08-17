def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num


def printRoman(number):
   result = ''
   num = [1, 4, 5, 9, 10, 40, 50, 90,
          100, 400, 500, 900, 1000]
   sym = ["I", "IV", "V", "IX", "X", "XL",
          "L", "XC", "C", "CD", "D", "CM", "M"]
   i = 12
   while number != 0:
      value = num[i]
      div = number // value
      number %= value
      for _ in range(div):
         result += sym[i]
      i -= 1
   return result

def PE089():
    return sum([len(line) - len(printRoman(romanToInt(line))) for line in open("PE089.txt").read().splitlines()])
print(PE089())
