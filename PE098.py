from collections import defaultdict
contents = open("PE098.txt").read()
contents = contents.split('","')
d = defaultdict(list)
[d[''.join(sorted(str(n * n)))].append(n * n) for n in range(10, 31662)]
[d.pop(k) for k in list(d.keys()) if len(d[k]) < 2]
mx = 0
found = 0
for word1 in contents:
    if len(word1) < found: continue
    for word2 in contents:
        if sorted(word1) == sorted(word2) and word1 != word2:
            for square in d.keys():
                if len(set(str(square))) != len(set(word1)) or len(str(square)) != len(word1):
                    continue
                for value in d[square]:
                    word = dict()
                    for letter in range(len(word1)): word[word1[letter]] = str(value)[letter]
                    newint = int(''.join([word[letter] for letter in word2]))
                    if newint in d[square]:
                        if mx < max(newint, value): mx = max(newint, value)
                        found = len(word1)
                        break
print(mx)