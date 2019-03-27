f = [1, 1]
d = []
for i in range(0, 31):
    f.append(f[-1] + f[-2])
    d.append(f[-1] / f[-2])
print(d)
print("=" * 80)
print(f)
