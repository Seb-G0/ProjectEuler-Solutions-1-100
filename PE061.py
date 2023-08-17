def generateOcta():
    octa = []
    for n in range(19, 60):
        octa.append(n * (3 * n - 2))
    return octa

def generateHepta():
    hepta = []
    for n in range(21, 64):
        hepta.append(n * (5*n-3)//2)
    return hepta

def generateHexa():
    hexa = []
    for n in range(23, 71):
        hexa.append(n * (2 * n - 1))
    return hexa

def generatePenta():
    penta = []
    for n in range(26, 82):
        penta.append(n * (3 * n - 1)// 2)
    return penta

def generateSquare():
    square = []
    for n in range(33, 100):
        square.append(n * n)
    return square

def generateTriangle():
    triangle = []
    for n in range(45, 141):
        triangle.append(n * (n + 1) // 2)
    return triangle
sq = generateSquare()
tr = generateTriangle()
hep = generateHepta()
pe = generatePenta()
oc = generateOcta()
hex = generateHexa()
possible = tr + sq + pe + hex + hep
def PE061():
    for n in oc:
        for p in possible:
            if str(n)[2:] == str(p)[:2]:
                for p2 in possible:
                    if str(p)[2:] == str(p2)[:2]:
                        for p3 in possible:
                            if str(p2)[2:] == str(p3)[:2]:
                                for p4 in possible:
                                    if str(p3)[2:] == str(p4)[:2]:
                                        for p5 in possible:
                                            if str(p4)[2:] == str(p5)[:2]:
                                                if str(p5)[2:] == str(n)[:2]:
                                                    s = [n, p, p2, p3, p4, p5]
                                                    for v in s:
                                                        if v in oc:
                                                            s.remove(v)
                                                            break
                                                    for v in s:
                                                        if v in hep:
                                                            s.remove(v)
                                                            break
                                                    for v in s:
                                                        if v in hex:
                                                            s.remove(v)
                                                            break
                                                    for v in s:
                                                        if v in pe:
                                                            s.remove(v)
                                                            break
                                                    for v in s:
                                                        if v in sq:
                                                            s.remove(v)
                                                            break
                                                    for v in s:
                                                        if v in tr:
                                                            s.remove(v)
                                                            break
                                                    if len(s) == 0:
                                                        return sum([n, p, p2, p3, p4, p5])

print(PE061())