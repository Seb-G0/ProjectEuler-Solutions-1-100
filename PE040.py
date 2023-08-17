i = 1
constant1 = "0"
while len(constant1) < 1000001:
    constant1 += str(i)
    i += 1
print(int(constant1[1]) * int(constant1[10]) * int(constant1[100]) * int(constant1[1000]) * int(constant1[10000]) * int(constant1[100000]) * int(constant1[1000000]))