P1 = input()
P2 = input()
p1 = P1.split()
p2 = P2.split()
x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])
D = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
print("%.4f" % D)
