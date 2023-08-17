before = dict()
contents = open("PE079.txt").read().splitlines()
for passcode in contents:
    for i in range(0, 3):
        digit = passcode[i]
        if digit not in before:
            before[digit] = set()
        for d in passcode[:i]:
            before[digit].add(d)
print(''.join(sorted(before, key=lambda k: len(before[k]))))