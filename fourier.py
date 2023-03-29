import numpy as np
import matplotlib.pyplot as plt
import math

# Variables
v = []
p = 0
A, B = [], []
a_out, b_out = [], []

# Full the Inputs
print("Enter The Voltage Values (): ")
while True:
    inp = input()
    if inp == "":
        break
    v.append(int(inp))
    p += 1

deg = np.linspace(30, 360, p, dtype=int)
# calculation
a0 = (1 / p) * (sum(v))
for i in range(1, 4):
    for n in range(0, p):
        a_out.append(v[n] * math.cos(i * deg[n] * (math.pi / 180)))
        b_out.append(v[n] * math.sin(i * deg[n] * (math.pi / 180)))
    A.append((2 / p) * sum(a_out))
    B.append((2 / p) * sum(b_out))
    a_out.clear()
    b_out.clear()

# Display Output

print("Degree = ", deg, "\nVoltage = ", v, "\na0 = ", "{:.2f}".format(a0), "\na1 = ", "{:.2f}".format(A[0]), "\na2 = ",
      "{:.2f}".format(A[1]), "\na3 = ", "{:.2f}".format(A[2]), "\nb1 = ", "{:.2f}".format(B[0]),
      "\nb2 = ", "{:.2f}".format(B[1]), "\nb3 = ", "{:.2f}".format(B[2]))

print(f'Equation:\nV = {"{:.2f}".format(a0)}+{"{:.2f}".format(A[0])}cosθ+{"{:.2f}".format(A[1])}cos2θ+{"{:.2f}".format(A[2])}cos3θ.....\n\t+{"{:.2f}".format(B[0])}sinθ+{"{:.2f}".format(B[1])}sin2θ+{"{:.2f}".format(B[2])}sin3θ.....')

# graph
plt.figure(figsize=(10, 5))
plt.plot(deg, v, "r")
plt.xlim(max(deg), 0)
plt.title("Fourier Series diagram", fontsize=16)
plt.xlabel("Degree", fontsize=14)
plt.ylabel("Voltage", fontsize=14)
plt.grid()
plt.show()

'''

62
35
-38
-64
-63
-52
-28
24
80
96
90
70

'''
