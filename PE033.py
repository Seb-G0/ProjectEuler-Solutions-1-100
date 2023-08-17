totalden = 1
totalnum = 1
for den in range(10,100):
    if den % 10 == 0:
        continue
    for num in range(10, den):
        if den//10 == num % 10:
            frac = num/den
            frac2 = (num // 10) / (den % 10)
            if frac == frac2:
                totalden *= den
                totalnum *= num
print(totalden/totalnum)