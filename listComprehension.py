C = [39, 0, 24, 3]
F = [ ((float(9)/5)*x + 32) for x in C ]

#print(F)

pythagorean_triple = [(x,y,z) for x in range(1,30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]

#print(pythagorean_triple)


