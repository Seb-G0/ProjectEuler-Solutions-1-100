from num2words import num2words
s = 0
for i in range(1,1001):
    string = num2words(i)
    while ' ' in string:
        string = string.replace(' ', '')
    while '-' in string:
        string = string.replace('-', '')
    s += len(string)
print(s)