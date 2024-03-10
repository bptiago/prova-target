# 3-a
# P.A, r = 2, (1, 3, 5, 7, 9)
sequencia_a = []
for i in range(1, 10, 2):
    sequencia_a.append(i)
print(sequencia_a)

# 3-b
# Seq. exponencial (2, 4, 8, 16, 32, 64)
sequencia_b = []
for i in range(1, 8):
    sequencia_b.append(2 ** i)
print(sequencia_b)

# 3-c
# 0, 1 (0 + 1), 4 (1 + 3), 9 (4 + 5), 16 (9 + 7), 25 (16 + 9), 36 (25 + 11), 49 (36 + 13)
sequencia_c = [0]
for i in range(1, 14, 2):
    sequencia_c.append(i + sequencia_c[-1])
print(sequencia_c)

# 3-d
# 4 (2**2), 16 (4**2), 36 (6**2), 64(8**2), 100 (10**2)
sequencia_d = []
for i in range (2, 11, 2):
    sequencia_d.append(i ** 2)
print(sequencia_d)

# 3-e
# 1, 1, 2, 3, 5, 8, 13, 21...
sequencia_e = [1, 1]
for i in range(5):
    sequencia_e.append(sequencia_e[-1] + sequencia_e[-2])
print(sequencia_e)

# 3-f
# 2, 10, 12, 16, 17, 18, 19, 200
# São números que iniciam com a letra "D"
